import axios from 'axios';
import React, {Component} from 'react';
import {Link, withRouter} from 'react-router-dom';
import settings from '../../../config/settings';
import './sidebar.scss';
//import logo from '../../../assets/images/logo-50.png';

class Sidebar extends Component {

    constructor(props) {
        super(props);
        this.state = {
            visible: true
        }
    }

    handleLogOutButton() {
        const {history} = this.props;

        axios({
            method: 'get',
            url: `${settings.API_ROOT}/logout`,
            withCredentials: true
        })
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
                Logout
            </button>

        )
    }

    render() {

        return (
            <div>
                <div className="ui huge menu stackable">

                <Link to={`/admin/`} className="item active">
                    {/* <img src={"../../../assets/images/logo-50.png"} className="mr-2"/> */}
                    <strong>Admin</strong>
                </Link>

                <Link to={`/admin/update`} className="item">Update Inventory</Link>


            <div className="right menu">

            {/* <div className="item">
                <div className="ui icon input form-group form-group-sm react-bs-table-search-form">
                    <input type="text" placeholder="Search..." className="form-control"/>
                    <i className="search icon"></i>
                </div>
            </div> */}
                <div className="item">
                    {this.renderLogOutButton()}
                </div>
            </div>
        </div>
    </div>

        )

    }
}

export default withRouter(Sidebar);
