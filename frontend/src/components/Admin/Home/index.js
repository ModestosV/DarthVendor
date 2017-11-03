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
            items:[{'modelNumber':'ZZZZZZZ',
            'quantity':46,
            'name':'Razer Desktop',
            'weight':15.0,
            'weightFormat':'lbs',
            'price':2299.99,
            'priceFormat':'CAD',
            'brandName':'RAZER',
            'type':'Desktop',
            'ramSize':16,
            'ramFormat':'GB',
            'processorType':'INTEL',
            'numCores':4,
            'hardDriveSize':2,
            'hardDriveFormat':'TB',
            'dx':15,
            'dy':30,
            'dz':1,
            'dimensionFormat':'INCH'}],
            errorMsg: null,
            showModal: false
        };
    }

    componentDidMount() {
        //this.itemsList();
    }

    itemsList() {
        return axios.get(`${settings.API_ROOT}/inventory`)
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
                    <BootstrapTable data={this.state.items} striped condensed hover pagination search scrolling>
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