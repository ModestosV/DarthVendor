import axios from 'axios';
import React, {Component} from 'react';
import {Link, withRouter} from 'react-router-dom';
import settings from '../../../config/settings';
import './sidebar.scss';


class Sidebar extends Component {

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

    renderToggleButton() {
        return (
            <button className="navbar-toggler collapsed" type="button" data-toggle="collapse" data-target="#myNavbar" aria-controls="myNavbar" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>   
        )
    }

    renderLogOutButton() {
        return (
   
            <button 
                className="btn btn-danger"
                onClick={() => this.handleLogOutButton()}
            >

            <span className="d-none d-md-inline">Log Out</span>
            
                {" "} 
                <i className="fa fa-sign-out" aria-hidden="true"></i>                                                
            </button>

        )
    }

    render() {
        return (    
            <div className="col-md-2 float-left col-1 pl-0 pr-0 collapse width show" id="sidebar">
                <div className="list-group border-0 card text-center text-md-left d-flex flex-column">
                <h5 className="pt-3"><span className="list-group-item d-none d-md-inline">Admin</span></h5>
                    
                    <Link to={`/`} className="list-group-item d-inline-block collapsed"><i className="fa fa-home"></i> <span className="d-none d-md-inline">Home</span></Link>

                    <a href="#products-menu" className="list-group-item d-inline-block collapsed" data-toggle="collapse" aria-expanded="false"><i className="fa fa-shopping-cart"></i> 
                    <span className="d-none d-md-inline">Products</span></a>
                    <div className="collapse" id="products-menu">
                        <Link to={`/inventory`} className="list-group-item">Inventory</Link>
                        <Link to={`/add`} className="list-group-item">Add new</Link>
                    </div>

                    <div className="mt-auto p-2">
                    {this.renderLogOutButton()}
                    </div>
     
                    {/* <a href="#" className="list-group-item d-inline-block collapsed" data-parent="#sidebar"><i className="fa fa-list"></i> <span className="d-none d-md-inline"></span></a> */}

                </div>
            </div>
        
        )
    }
}

export default withRouter(Sidebar);