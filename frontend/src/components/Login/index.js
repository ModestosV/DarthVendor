import axios from 'axios';
import React, {Component} from 'react';
import swal from 'sweetalert';
import settings from '../../config/settings';
import './Login.scss';


class Login extends Component {

    constructor(props) {
        super(props);

        this.state = {
            username: '',
            password: '',
            adminCheatCode: [38, 38, 40, 40, 37, 39, 37, 39, 65, 66, 65, 66],  // Up, Up, Down, Down, Left, Right, Left, Right, A, B, A, B
            cancelAdminCheatCode: [81], // Q
            keyStroke: [],
            isAdminLogin: false
        }
    }

    handleUserNameChange(event) {
        this.setState({username: event.target.value});
    }

    handlePasswordChange(event) {
        this.setState({password: event.target.value});
    }

    handleForm() {
        const {dispatch, history} = this.props;

        let data = {
            'username': this.state.username,
            'password': this.state.password
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
            console.log(response.data);
            localStorage.setItem('activeUser', JSON.stringify(response.data));                        
            history.push('/');
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
                swal({
                    title: "Darth Varder Mode",
                    text: "Admin login enabled. Remember, this power is privilege.",
                    icon: "warning",
                    button: "Ok"                    
                })   
                                      
                this.setState({keyStroke: [], isAdminLogin: true});
            } else if (this.state.isAdminLogin && this.state.keyStroke.join(',').includes(this.state.cancelAdminCheatCode.join(','))) {                
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
    }

    componentWillUnmount() {
        document.removeEventListener("keydown", (e) =>this.onKeyPressHandler(e), false);
    }

    render() {

        return (
            <div className="container">
                <div className="row">
                    <div className="col-md-4" />
                    <div className="col-md-4" style={{marginTop: '30%'}}>
                        <div id="login">
                            <div>
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
                                        placeholder="Username"
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
                                <button
                                    type="button"
                                    className="btn btn-dark btn-block"
                                    onClick={() => this.handleForm()}
                                >
                                    Login <i className="fa fa-sign-in"></i>
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default Login;
