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
            isAdminLogin: false,
            toggleRegister: false,
        }
    }

    handleUserNameChange(event) {
        this.setState({username: event.target.value});
    }

    handlePasswordChange(event) {
        this.setState({password: event.target.value});
    }


    registerHandleFirstName(event){
        this.setState({registerFirst: event.target.value});
    }

    registerHandleLasttName(event){
        this.setState({registerLast: event.target.value});
    }

    registerHandleEmail(event){
        this.setState({registerEmail: event.target.value});

        if (/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(this.state.registerEmail)){
            console.log("good email");
            this.setState({errorEmail: false});
        }else{
            console.log("Bad");
            this.setState({errorEmail: true});

        }
    }

    registerHandleAddress(event){
        this.setState({registerAddress: event.target.value});
    }
    
    registerHandlePhone(event){
        this.setState({registerPhone: event.target.value});

        if(/\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})/.test(this.state.registerPhone)){
            console.log("good phone");
            this.setState({errorPhone: false});
        }else{
            console.log("bad phone");
            this.setState({errorPhone: true});
        }
    }

    registerHandlePassword(event){
        this.setState({registerPassword: event.target.value});

        if(/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/.test(this.state.registerPassword)){
            console.log("good password");
            this.setState({errorPassword: false});
        }else{
            console.log("bad password");
            this.setState({errorPassword: true});
        }
    }

    handleRegisterForm(){

        let data = {
            'first': this.state.registerFirst,
            'last': this.state.registerLast,
            'email': this.state.registerEmail,
            'address': this.state.registerAddress,
            'phone': this.state.registerPhone,
            'password': this.state.registerPassword,
            'isAdmin': false
        };

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

        if (this.state.toggleRegister){
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
                        <li className={passwordMsg}>Password must be a minimum eight characters, at least one letter and one number</li>
                    </ul>
                </div>


                <div id="register" className="d-flex justify-content-end">
                        Have an account? <span className="" onClick={() => this.toggleForm()}> Login.</span> 
                </div>
            </div>
            );
        }
    }

    loginForm(){
        if (!this.state.toggleRegister){
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
                    <button
                        type="button"
                        className="btn btn-dark btn-block"
                        onClick={() => this.handleLoginForm()}
                    >
                        Login <i className="fa fa-sign-in"></i>
                    </button>
                </form>
                <div id="register" className="d-flex justify-content-end">
                        Don't have an account? <span className="" onClick={() => this.toggleForm()}> Sign up now!</span> 
                </div>
            </div>
            );
        }
    }

    toggleForm(){
        this.setState({toggleRegister: !this.state.toggleRegister})
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
                <div className="form__body d-flex justify-content-center align-items-center">
                    <div className="wrapper">
                        {this.loginForm()}
                        {this.registerForm()}
                    </div>
                </div>
            </div>
        )
    }
}

export default Login;
