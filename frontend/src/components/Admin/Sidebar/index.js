import axios from 'axios';
import React, {Component} from 'react';
import {Link, withRouter} from 'react-router-dom';
import settings from '../../../config/settings';
import './sidebar.scss';

class Sidebar extends Component {

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
                className="ui inverted basic button"
                onClick={() => this.handleLogOutButton()}
            >
        

            
                {" "} 
                <i className="external icon" aria-hidden="true"></i>    
                Logout                                            
            </button>

        )
    }

    render() {

        let sidebarClass = "ui left vertical inverted sidebar labeled icon menu d-flex flex-column";
        
        if(this.state.visible) {
            sidebarClass += " visible";
        }

        return (    
            <div className={sidebarClass}>
                <Link to={`/`} className="item">
                    <i className="home icon"></i>
                    Home
                </Link>
                <Link to={`/inventory`} className="item">
                    <i className="shopping bag icon"></i>
                    Inventory
                </Link>



               <div className="mt-auto p-2">
                        {this.renderLogOutButton()}
                </div> 
            </div>

        
        )
        
    }
}

export default withRouter(Sidebar);