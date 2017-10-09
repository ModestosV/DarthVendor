import axios from 'axios';
import React, {Component} from 'react';
import swal from 'sweetalert';
import settings from '../../../config/settings';
import './Login.scss';


class Login extends Component {    

    constructor(props) {
        super(props);

        this.state = {
            username: '',
            password: ''
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

        axios.post(`${settings.API_ROOT}/login`, data)
            .then(response => {
                console.log(response.data);
                localStorage.setItem('activeUser', JSON.stringify(response.data));
                history.push('/');
            })
            .catch(error => {
                console.log(error);
                swal({
                    title: "Woops!",
                    text: "Please provide valid credentials.",
                    icon: "error",
                    button: "Ok",
                });                 
            })
    }

    componentWillMount() {        
        console.log(localStorage);
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