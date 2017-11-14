import axios from 'axios';
import React, {Component} from 'react';
import {Link, withRouter} from 'react-router-dom';
import swal from 'sweetalert';
import settings from '../../config/settings';
import '../Login/Login.scss';

class Register extends Component {

    constructor(props) {
        super(props);
        this.state = {}
    }

    registerHandleFirstName(event){
        this.setState({registerFirst: event.target.value});
    }

    registerHandleLasttName(event){
        this.setState({registerLast: event.target.value});
    }

    registerHandleUsername(event){
        this.setState({registerUsername: event.target.value});
    }

    registerHandleEmail(event){
        this.setState({registerEmail: event.target.value});

        if (/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(this.state.registerEmail)){
            this.setState({errorEmail: false});
        }else{
            this.setState({errorEmail: true});
        }
    }

    registerHandleAddress(event){
        this.setState({registerAddress: event.target.value});
    }
    
    registerHandlePhone(event){
        this.setState({registerPhone: event.target.value});

        if(/^[+]*[(]{0,1}[0-9]{1,3}[)]{0,1}[-\s\./0-9]*$/g.test(this.state.registerPhone)){
            this.setState({errorPhone: false});
        }else{
            this.setState({errorPhone: true});
        }
    }

    registerHandlePassword(event){
        this.setState({registerPassword: event.target.value});

        if(/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/.test(this.state.registerPassword)){
            this.setState({errorPassword: false});
        }else{
            this.setState({errorPassword: true});
        }
    }

    handleRegisterForm(){
        let data = {
            'firstname': this.state.registerFirst,
            'lastname': this.state.registerLast,
            'username': this.state.registerUsername,
            'email': this.state.registerEmail,
            'address': this.state.registerAddress,
            'phone': this.state.registerPhone,
            'password': this.state.registerPassword
        };
        
        axios({
            method: 'post',
            url: `${settings.API_ROOT}/register`,
            data: data
        })
        .then(response => {
            swal("Congratulation! You are now registered!");
            history.push('/');            
        })
        .catch(error => {
            if (error.request.status === 401) {
                swal({
                    title: "Uh oh!",
                    text: "Some email cannot be registered twice.",
                    icon: "error",
                    button: "Ok",
                });
            } else {
                swal({
                    title: "Woops!",
                    text: "Something is wrong!",
                    icon: "error",
                    button: "Ok",
                });
            }
        })
        // axios({
        //     method: 'post',
        //     url: `${settings.API_ROOT}/login`,
        //     data: data,
        //     withCredentials: true
        // })
        // .then(response => {
        //     // console.log(response.datan);
        //     localStorage.setItem('activeUser', JSON.stringify(response.data));

        //     if(response.data.isAdmin === true) {
        //         history.push('/admin');
        //     } else {
        //         history.push('/');
        //     }
            
        // })
        // .catch(error => {
        //     if (error.request.status === 401) {
        //         swal({
        //             title: "Uh oh!",
        //             text: "Are you lost?",
        //             icon: "error",
        //             button: "Ok",
        //         });
        //     } else {
        //         swal({
        //             title: "Woops!",
        //             text: "Please try registering again!",
        //             icon: "error",
        //             button: "Ok",
        //         });
        //     }
        // })
    
    }

    registerForm(){

        let email, phone, password;
        email = phone = password = "form-control";

        let emailMsg, phoneMsg, passwordMsg;
        emailMsg = phoneMsg = passwordMsg = "list-group-item hidden";

        let button = "btn btn-dark btn-block disabled";

        if (this.state.errorEmail){
            email = "form-control input--error";
            emailMsg = "list-group-item";
        }
        if (this.state.errorPhone){
            phone = "form-control input--error";
            phoneMsg = "list-group-item";
        }
        if (this.state.errorPassword){
            password = "form-control input--error";
            passwordMsg = "list-group-item";
        }

        if (!this.state.errorEmail && !this.state.errorPhone && !this.state.errorPassword){
            button = "btn btn-dark btn-block"
        }

        return (
            
            <div id="register">
            <div className="header">
                <h1> Register </h1>
            </div>
            <form>
                <div className="input-group mb-3">
                    <div className="input-group-addon">
                        First name
                    </div>
                    <input
                        type="text"
                        className="form-control"
                        placeholder="Darth"
                        onChange={(e) => this.registerHandleFirstName(e)}
                    />
                </div>
                <div className="input-group mb-3">
                    <div className="input-group-addon">
                        Last name
                    </div>
                    <input
                        type="text"
                        className="form-control"
                        placeholder="Vador"
                        onChange={(e) => this.registerHandleLasttName(e)}
                    />
                </div>
                <div className="input-group mb-3">
                    <div className="input-group-addon">
                        Username
                    </div>
                    <input
                        type="text"
                        className="form-control"
                        placeholder="darthvador"
                        onChange={(e) => this.registerHandleUsername(e)}
                    />
                </div>
                <div className="input-group mb-3">
                    <div className="input-group-addon">
                        <i className="fa fa-envelope"></i>
                    </div>
                    <input
                        type="email"
                        className={email}
                        placeholder="darthvador@hotmail.com"
                        onChange={(e) => this.registerHandleEmail(e)}
                    />
                </div>


                <div className="input-group mb-3">
                    <div className="input-group-addon">
                        <i className="fa fa-home"></i>
                    </div>
                    <input
                        type="text"
                        className="form-control"
                        placeholder="Concordia University, QC, Canada"
                        onChange={(e) => this.registerHandleAddress(e)}
                    />
                </div>


                <div className="input-group mb-3">
                    <div className="input-group-addon">
                        <i className="fa fa-phone"></i>
                    </div>
                    <input
                        type="text"
                        className={phone}
                        placeholder="514-123-4567"
                        onChange={(e) => this.registerHandlePhone(e)}
                    />
                </div>

                <div className="input-group mb-3">
                    <div className="input-group-addon">
                    <i className="fa fa-lock"></i>
                    </div>
                    <input
                        type="password"
                        className={password}
                        placeholder="topsecret"
                        onChange={(e) => this.registerHandlePassword(e)}
                    />
                </div>

                <button
                    type="email"
                    className={button}
                    onClick={() => this.handleRegisterForm()}
                >
                    Sign up <i className="fa fa-sign-in"></i>
                </button>
            </form>

            <div className="error--message">
                <ul className="list-group">
                    <li className={emailMsg}>Invalid Email Address</li>
                    <li className={phoneMsg}>Invalid Phone Number</li>
                    <li className={passwordMsg}>Password must be a minimum nine characters, at least two letter and two number</li>
                </ul>
            </div>


            <div id="register" className="d-flex justify-content-end mt-2">
                    Have an account? <Link className="link" to={`/login`}> Login.</Link> 
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

    render() {
        return (
            <div className="container">
                <div className="form__body d-flex justify-content-center align-items-center">
                    <div className="wrapper">
                        {this.registerForm()}
                    </div>
                </div>
            </div>
        )
    }
}

export default Register;
