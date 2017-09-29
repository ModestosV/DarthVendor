import axios from 'axios';
import React, {Component} from 'react';
import {Link, HashRouter as Router, Route} from 'react-router-dom';
import settings from '../../../config/settings';
import Sidebar from '../Sidebar';
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';

class Inventory extends Component {

    constructor(props) {
        super(props);
        this.state = {
            items: [],
            errorMsg: null
        };
    }

    componentWillMount() {  
        const {history} = this.props;      
        console.log(localStorage);
        if (!localStorage.activeUser) {
            history.push('/login');
        }
    }

    componentDidMount() {
        this.itemsList();
    }

    itemsList() {
        return axios.get(`${settings.API_ROOT}/itemsList`)
        .then(results => {
            const errorMsg = null;
            const items = results.data.map(item => item);
            this.setState({items});
            this.setState({errorMsg});
            console.log(items);
        })
        .catch(error => {
         console.log(error);
         const errorMsg = "Oops, something went wrong while fetching items!";
         this.setState({errorMsg});
       })
    }
    render() {
        function cellFormat(cell, row){
            return '<i class="glyphicon glyphicon-usd"></i> ' + cell;
        }
        return (
            <div>
                <Sidebar />
                <div className="col-md-10 float-left col px-5 pl-md-2 pt-2 main">
                    <link rel="stylesheet" href="https://npmcdn.com/react-bootstrap-table/dist/react-bootstrap-table-all.min.css"></link>
                    <a href="#" data-target="#sidebar" data-toggle="collapse"><i className="fa fa-navicon fa-2x py-2 p-1"></i></a>
                    <h1> Inventory </h1>
                    { !!this.state.errorMsg && <div className="fa fa-warning errorMsg"> {this.state.errorMsg} </div> }
                    <br />
                    <Link to={`/inventory/add`} className="list-group-item d-inline-block collapsed"><i className="fa fa-plus"></i> <span className="d-none d-md-inline">Add Item</span></Link>
                    <BootstrapTable data={this.state.items} striped condensed hover pagination search>
                        <TableHeaderColumn dataField="quantity" dataAlign="center" dataSort={true} dataFormat={cellFormat}>Quantity</TableHeaderColumn>
                        <TableHeaderColumn dataField="brandName" isKey={true} dataSort={true} dataAlign="center" dataSort={true} dataFormat={cellFormat}>Brand Name</TableHeaderColumn>
                        <TableHeaderColumn dataField="modelNumber" dataAlign="center" dataSort={true} dataFormat={cellFormat}>Model Number</TableHeaderColumn>
                        <TableHeaderColumn dataField="weight" dataSort={true} dataAlign="center" dataSort={true} dataFormat={cellFormat}>Weight</TableHeaderColumn>
                        <TableHeaderColumn dataField="weightFormat" dataSort={true} dataAlign="center" dataSort={true} dataFormat={cellFormat}>Weight Format</TableHeaderColumn>
                        <TableHeaderColumn dataField="price" dataSort={true} dataAlign="center" dataSort={true} dataFormat={cellFormat}>Price</TableHeaderColumn>
                        <TableHeaderColumn dataField="priceFormat" dataSort={true} dataAlign="center" dataSort={true} dataFormat={cellFormat}>Price Format</TableHeaderColumn>
                        <TableHeaderColumn dataField="type" dataSort={true} dataAlign="center" dataSort={true} dataFormat={cellFormat}>Type</TableHeaderColumn>
                    </BootstrapTable>
                </div>
            </div>
        );
    }
}

export default Inventory;