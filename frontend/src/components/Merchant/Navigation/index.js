import axios from 'axios';
import React, {Component} from 'react';
import {Link, withRouter} from 'react-router-dom';
import settings from '../../../config/settings';
import './Navigation.scss';
import logo from '../../../assets/images/logo-50.png';

class Navigation extends Component {

    constructor(props) {
        super(props);
        this.state = {
            visible: true
        }
    }

    handleLogOutButton() {
        const {history} = this.props;
        let headers = {
            'authorization': JSON.parse(localStorage.activeUser)['token'] 
        };        
        let config = {
            'headers': headers
        };
        
        axios.get(`${settings.API_ROOT}/logout`, config)
            .then(response => {
                console.log(response);
                localStorage.setItem('activeUser', '');
                history.push('/login');
            })
            .catch(error => {
                console.log(error);                
            })
    }

    renderLogOutButton() {
        return (
   
            <button 
                className="ui primary button"
                onClick={() => this.handleLogOutButton()}
            >
                {" "}    
                Login                                         
            </button>

        )
    }

    render() {

        return (    
            <div>
                <div className="ui huge menu stackable">

                <Link to={`/merchant`} className="item active">
                    <img src={logo} className="mr-2"/>
                </Link>

                <Link to={`/merchant`} className="item">Catalog</Link>


            <div className="right menu">

            {/* <div className="item">
                <div className="ui icon input form-group form-group-sm react-bs-table-search-form">
                    <input type="text" placeholder="Search..." className="form-control"/>
                    <i className="search icon"></i>
                </div>
            </div> */}
                <Link to={`/cart`} className="item">
                    <i className="shopping basket icon mx-auto"></i>
                </Link>
                <div className="item">
                    {this.renderLogOutButton()}
                </div>
            </div>
        </div>
    </div>   
        
        )
        
    }
}

export default withRouter(Navigation);