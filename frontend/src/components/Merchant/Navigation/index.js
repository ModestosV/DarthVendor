import axios from 'axios';
import React, {Component} from 'react';
import { Dropdown, Menu } from 'semantic-ui-react'
import {Link, withRouter} from 'react-router-dom';
import swal from 'sweetalert';
import settings from '../../../config/settings';
import './Navigation.scss';
import logo from '../../../assets/images/logo-50.png';

class Navigation extends Component {

    constructor(props) {
        super(props);
        this.state = {
            log: false,
            visible: true
        }
    }

    handleLogOutButton() {
        swal({
            title: "Log out?",
            text: "Are you sure you want log out?",            
            type: "warning",
            buttons: {
                confirm:true,
                cancel: true
            }            
          })
          .then((confirm) => {   
                if(confirm){
                    const {history} = this.props;
            
                    axios({
                        method: 'get',        
                        url: `${settings.API_ROOT}/logout`,
                        withCredentials: true
                    })        
                    .then(response => {        
                        console.log(response);        
                        localStorage.setItem('activeUser', '');
                        history.push('/');
                        this.setState({log: false})      
                    })        
                    .catch(error => {        
                        console.log(error);
                    });
                }
            });
    
    }

    handleReturnButton() {
        const {history} = this.props;
        history.push('/return');
    }

    handleDeleteAccount() {

        swal({
              title: "Delete account?",
              text: "Are you sure you want to delete your account?",
              type: "warning",
              buttons: {
                  confirm:true,
                  cancel: true
              }
            })
            .then((confirm) => {
                if(confirm){
                    axios({
                        method: 'post',
                        url: `${settings.API_ROOT}/deleteAccount`,
                        withCredentials: true,
                    })
                    .then(response => {
                        swal("Deleted!", "Your account has been deleted.", "success");
                        localStorage.removeItem("activeUser");
                        this.props.history.push("/")
                    })
                    .catch(error => {
                        console.log(error);
                        swal({
                            title: "Woops!",
                            text: "Something went wrong!",
                            ilcon: "error",
                            button: "Ok",
                        });
                    })
                }
            });
    }

    renderLogBtn(){
        if(localStorage.activeUser){
            return (
                <Dropdown text='Account' className='ui primary button'>
                    <Dropdown.Menu>
                        <Dropdown.Item onClick={() => this.handleLogOutButton()}>Logout</Dropdown.Item>
                        <Dropdown.Item onClick={() => this.handleReturnButton()}>Return Item</Dropdown.Item>
                        <Dropdown.Divider />
                        <Dropdown.Item onClick={() => this.handleDeleteAccount()}>Delete Account</Dropdown.Item>
                    </Dropdown.Menu>
                </Dropdown>
            )
        } else {
            return (
                <Link to={`/login`} className="item">Login</Link>
            )
        }
        
    }

    renderCart(){
        if(this.state.log){
            return (
                <Link to={`/cart`} className="item">
                    <i className="shopping basket icon mx-auto"></i>
                </Link>
            )
        }
    }

    componentDidMount() {
        if(localStorage.activeUser) {
            this.setState({log: true});
        }
    }

    render() {


        return (
            <div>
                <div className="ui huge menu stackable">

                <Link to={`/`} className="item active">
                    <img src={logo} className="mr-2"/>
                </Link>

                <Link to={`/`} className="item">Catalog</Link>

            <div className="right menu">

            {/* <div className="item">
                <div className="ui icon input form-group form-group-sm react-bs-table-search-form">
                    <input type="text" placeholder="Search..." className="form-control"/>
                    <i className="search icon"></i>
                </div>
            </div> */}
                {this.renderCart()}
                <div className="item">
                    {this.renderLogBtn()}
                </div>
            </div>
        </div>
    </div>

        )

    }
}

export default withRouter(Navigation);
