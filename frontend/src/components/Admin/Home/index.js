import axios from 'axios';
import React, {Component} from 'react';
import {Link, HashRouter as Router, Route} from 'react-router-dom';
import settings from '../../../config/settings';
import Sidebar from '../Sidebar';
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';

class Home extends Component {

    constructor(props) {
        super(props);
        this.state = {
            items:[],
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

            if (activeUser.isAdmin === false) {
                // Redirect to merchant home page                
                history.push('merchant');
            }            
        }        
    }

    componentDidMount() {
        this.itemsList();
    }

    itemsList() {
        return axios({
            method:'get',
            url: `${settings.API_ROOT}/inventory`,
            withCredentials: true
        })
        .then(results => {
            const errorMsg = null;
            const items = results.data.map(item => item);
            const itemsList = items;
            this.setState({itemsList});
            this.setState({items});
            this.setState({errorMsg});
            console.log(this.state);
        })
        .catch(error => {
         console.log(error);
         const errorMsg = "Oops, something went wrong while fetching items!";
         this.setState({errorMsg});
       })
    }

    filterItems(e) {
        if(e.target.value == ""){
            this.setState({itemsList: this.state.items});
        } else {
            let filteredItems = this.state.items.filter(item => item.weight < e.target.value);
            this.setState({itemsList: filteredItems});
        }
        
    }

    render() {

        function cellFormat(cell, row){
            return '<i class="glyphicon glyphicon-usd"></i> ' + cell;
        }

        function sortFunc(a, b, order) {
            if (order === 'desc') {
                return a.price - b.price;
            } else {
                return b.price - a.price;
            }
        }

        return (
            <div>
                <Sidebar />
                <div className="container">
                    <link rel="stylesheet" href="https://npmcdn.com/react-bootstrap-table/dist/react-bootstrap-table-all.min.css"></link>
                    <h1> Inventory </h1>
                    { !!this.state.errorMsg && <div className="fa fa-warning errorMsg"> {this.state.errorMsg} </div> }
                    <br />
                    <input type="text" onBlur={(e) => this.filterItems(e)}/>
                    <BootstrapTable data={this.state.itemsList} striped condensed hover pagination search scrolling>
                        <TableHeaderColumn dataField="modelNumber" dataAlign="center" dataSort={true} dataFormat={cellFormat}>Model Number</TableHeaderColumn>
                        <TableHeaderColumn dataField="brandName" isKey={true} dataAlign="center" dataSort={true} dataFormat={cellFormat}>Brand Name</TableHeaderColumn>
                        <TableHeaderColumn dataField="type" dataAlign="center" dataSort={true} dataFormat={cellFormat}>Type</TableHeaderColumn>
                        <TableHeaderColumn dataField="weight" dataAlign="center" dataSort={true} dataFormat={cellFormat}>Weight</TableHeaderColumn>
                        <TableHeaderColumn dataField="weightFormat" dataAlign="center" dataSort={true} dataFormat={cellFormat}>Weight Format</TableHeaderColumn>
                        <TableHeaderColumn dataField="price" dataAlign="center" dataSort={true} sortFunc={sortFunc} dataFormat={cellFormat}>Price</TableHeaderColumn>
                        <TableHeaderColumn dataField="priceFormat" dataAlign="center" dataSort={true} dataFormat={cellFormat}>Price Format</TableHeaderColumn>
                        <TableHeaderColumn dataField="quantity" dataAlign="center" dataSort={true} dataFormat={cellFormat}>Quantity</TableHeaderColumn>
                    </BootstrapTable>
                </div>
            </div>
        );
    }
}

export default Home
