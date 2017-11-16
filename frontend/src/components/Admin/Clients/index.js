import axios from 'axios';
import React, {Component} from 'react';
import {Link, HashRouter as Router, Route} from 'react-router-dom';
import settings from '../../../config/settings';
import Sidebar from '../Sidebar';
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';

class Clients extends Component {

    constructor(props) {
        super(props);
        this.state = {
            clients:[],
            errorMsg: null,
            showModal: false
        };
    }

    componentWillMount() {
        console.log(localStorage);
        
        const {dispatch, history} = this.props;
        
        // Redirect if user is not logged in
        if (!localStorage.activeUser) {
            history.push('/login');
        } else {
            const activeUser = JSON.parse(localStorage.activeUser);
            if (activeUser.adminPermission === false) {
                // Redirect to merchant home page                
                history.push('/');
            }            
        }        
    }

    componentDidMount() {
        this.clientsList();
    }

    clientsList() {
        return axios.get(`${settings.API_ROOT}/viewCustomers`)
        .then(results => {
            const errorMsg = null;
            const clients = results.data.map(client => client);
            this.setState({clients});
            this.setState({errorMsg});
            console.log(clients);
        })
        .catch(error => {
         console.log(error);
         const errorMsg = "Oops, something went wrong while fetching clients!";
         this.setState({errorMsg});
       })
    }

    render() {

        return (
            <div>
                <Sidebar />
                <div className="container mb-5">
                    <link rel="stylesheet" href="https://npmcdn.com/react-bootstrap-table/dist/react-bootstrap-table-all.min.css"></link>
                    <h1> Clients List </h1>
                    { !!this.state.errorMsg && <div className="fa fa-warning errorMsg"> {this.state.errorMsg} </div> }
                    <br />
                    <BootstrapTable data={this.state.clients} striped condensed hover search scrolling>
                        <TableHeaderColumn dataField="email" dataAlign="center" dataSort={true}>Email</TableHeaderColumn>
                        <TableHeaderColumn dataField="username" isKey={true} dataAlign="center" dataSort={true}>Username</TableHeaderColumn>
                        <TableHeaderColumn dataField="lastname" dataAlign="center" dataSort={true}>Last Name</TableHeaderColumn>
                        <TableHeaderColumn dataField="firstname" dataAlign="center" dataSort={true}>First Name</TableHeaderColumn>
                        <TableHeaderColumn dataField="address" dataAlign="center" dataSort={true}>Address</TableHeaderColumn>
                        <TableHeaderColumn dataField="phone" dataAlign="center" dataSort={true}>Phone</TableHeaderColumn>
                    </BootstrapTable>
                </div>
            </div>
        );
    }
}

export default Clients
