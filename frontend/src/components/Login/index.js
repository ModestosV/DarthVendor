import axios from 'axios';
import React, {Component} from 'react';
import settings from '../../config/settings';
import {Link, withRouter} from 'react-router-dom';
import {Checkbox} from 'semantic-ui-react'
import swal from 'sweetalert';
import './Login.scss';
import ls from './lightsaber.mp3';
import breath from './breath.mp3';


class Login extends Component {

    constructor(props) {
        super(props);

        this.state = {
            username: '',
            password: '',
            adminCheatCode: [38, 38, 40, 40, 37, 39, 37, 39, 65, 66, 65, 66],  // Up, Up, Down, Down, Left, Right, Left, Right, A, B, A, B
            cancelAdminCheatCode: [81], // Q
            keyStroke: [],
            isAdminLogin: false,
        }

        this.soundLS = new Audio(ls);
        this.soundBreath = new Audio(breath);
    }

    handleUserNameChange(event) {
        this.setState({username: event.target.value});
    }

    handlePasswordChange(event) {
        this.setState({password: event.target.value});
    }

    // handleToggle(event, data) {        
    //     this.setState({isAdminLogin: data.checked});
        
    //     if (data.checked) {
    //         swal({
    //             title: "Darth Vendor Mode",
    //             text: "Admin login enabled. Remember, this power is privilege.",
    //             icon: "warning",
    //             button: "Ok"
    //         })
    //     } else { 
    //         swal({
    //             title: "Stormtrooper Mode",
    //             text: "Admin login disabled.",
    //             icon: "warning",
    //             button: "Ok"
    //         })  
    //     }      
    // }

    handleLoginForm() {
        const {dispatch, history} = this.props;
        
        let data = {
            'email': this.state.username,
            'password': this.state.password,
            'isAdmin': false
        };

        if (this.state.isAdminLogin) {
            data['isAdmin'] = true;
        }

        axios({
            method: 'post',
            url: `${settings.API_ROOT}/login`,
            data: data,
            withCredentials: true
        })
        .then(response => {
            // console.log(response.datan);
            localStorage.setItem('activeUser', JSON.stringify(response.data));

            if(response.data.isAdmin === true) {
                history.push('/admin');
            } else {
                history.push('/');
            }
            
        })
        .catch(error => {
            if (error.request.status === 401) {
                swal({
                    title: "Uh oh!",
                    text: "Are you lost?",
                    icon: "error",
                    button: "Ok",
                });
            } else {
                swal({
                    title: "Woops!",
                    text: "Please provide valid credentials.",
                    icon: "error",
                    button: "Ok",
                });
            }
        })
    }

    onKeyPressHandler(event) {
        this.setState((state) => {
            return {keyStroke: [...this.state.keyStroke, event.keyCode]}
        },
        () => {
            if (this.state.keyStroke.join(',').includes(this.state.adminCheatCode.join(','))) {
                this.soundLS.play();
                this.soundBreath.play();
                swal({
                    title: "Darth Vendor Mode",
                    text: "Admin login enabled. Remember, this power is privilege.",
                    icon: "warning",
                    button: "Ok"
                })

                this.setState({keyStroke: [], isAdminLogin: true});
            } else if (this.state.isAdminLogin && this.state.keyStroke.join(',').includes(this.state.cancelAdminCheatCode.join(','))) {
                this.soundLS.play();
                this.soundBreath.pause();
                swal({
                    title: "Stormtrooper Mode",
                    text: "Admin login disabled.",
                    icon: "warning",
                    button: "Ok"
                })
                this.setState({keyStroke: [], isAdminLogin: false});
            }

        });
    }

    handleCheckboxAdmin(){
        this.soundLS.play();
        if(this.state.isAdminLogin){
           this.soundBreath.pause();
           this.soundBreath.currentTime = 0;
           this.setState({isAdminLogin: false});
           swal({
            title: "Stormtrooper Mode",
            text: "Admin login disabled.",
            icon: "warning",
            button: "Ok"
            }); 
       } else {
        this.soundBreath.play();
        this.setState({isAdminLogin: true});
        swal({
            title: "Darth Vendor Mode",
            text: "Admin login enabled. Remember, this power is privilege.",
            icon: "warning",
            button: "Ok"
        });
       }
    }
    loginForm(){
        
        let toggleButton = (
            // <div className="d-flex justify-content-end" style={{}}>
            //     <label style={{fontWeight: '600', padding: '0 5px 0 5px'}}> Admin </label>
            //     <Checkbox 
            //         toggle                     
            //         onClick={(e, d) => this.handleToggle(e, d)}
            //     />
            // </div>

            <div className="lightsaber">
                <label htmlFor="darth-vader-example"></label>
                <input type="checkbox" id="darth-vader-example" checked={this.state.isAdminLogin}
                onClick={() => this.handleCheckboxAdmin()}/>
                <div className="switch"></div>
                <div className="plasma vader"></div>
            </div>
        )


        return (   
            <div id="login">
            <div className="header">
                <h1> Login </h1>
            </div>
            <form>
                <div className="input-group mb-3">
                    <div className="input-group-addon">
                        <i className="fa fa-user"></i>
                    </div>
                    <input
                        type="text"
                        className="form-control"
                        placeholder="Email"
                        onChange={(e) => this.handleUserNameChange(e)}
                    />
                </div>
                <div className="input-group mb-3">
                    <div className="input-group-addon">
                        <i className="fa fa-lock"></i>
                    </div>
                    <input
                        type="password"
                        className="form-control"
                        placeholder="Password"
                        onChange={(e) => this.handlePasswordChange(e)}
                    />
                </div>
                {toggleButton}

                <button
                    type="button"
                    className="btn btn-dark btn-block"
                    onClick={() => this.handleLoginForm()}
                >
                    Login <i className="fa fa-sign-in"></i>
                </button>
            </form>
            <div id="register" className="d-flex justify-content-end mt-3">
                <span style={{color:'white'}}> Don't have an account? </span> <Link className="link" to={`/register`}> Sign up now.</Link> 
            </div>
        </div>
        );
    }

    componentWillMount() {
        console.log(localStorage);

        const {dispatch, history} = this.props;

        if (localStorage.activeUser) {
            const activeUser = JSON.parse(localStorage.activeUser);

            if (activeUser.isAdmin === true) {
                // Redirect to admin home page
                history.push('/admin/');
            } else {
                // Redirect to merchant home page
                history.push('/');
            }
        }
    }

    componentDidMount() {
        document.addEventListener("keydown", (e) =>this.onKeyPressHandler(e), false);
        document.body.classList.add("body_bg");
        var movementStrength = 25;
        var height = movementStrength / $(window).height();
        var width = movementStrength / $(window).width();
        $(".body_bg").mousemove((e) => {
                  var pageX = e.pageX - ($(window).width() / 2);
                  var pageY = e.pageY - ($(window).height() / 2);
                  var newvalueX = width * pageX * -1 - 25;
                  var newvalueY = height * pageY * -1 - 50;
                  $('.body_bg').css("background-position", newvalueX+"px     "+newvalueY+"px");
        });
    }

    componentWillUnmount() {
        document.removeEventListener("keydown", (e) =>this.onKeyPressHandler(e), false);
        document.body.classList.remove("body_bg");
    }

    render() {
        return (
            <div className="container">
                <div className="form__body d-flex justify-content-center align-items-center">
                    <div className="wrapper">
                        {this.loginForm()}
                    </div>
                </div>
                {/* <audio id="audio">
                    <source src="./lightsaber" type="audio/mpeg"/>
                </audio>  */}
            </div>
        )
    }
}

export default Login;
