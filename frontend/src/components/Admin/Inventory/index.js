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
                <div className="pusher">
                    <div className="mt-4">
                        <link rel="stylesheet" href="https://npmcdn.com/react-bootstrap-table/dist/react-bootstrap-table-all.min.css"></link>
                        <h1 className="m-0"> Inventory </h1>
                        { !!this.state.errorMsg && <div className="fa fa-warning errorMsg"> {this.state.errorMsg} </div> }
                        <br />
                        <Link to={`/inventory/add`} className="list-group-item d-inline-block collapsed">
                            <i className="fa fa-plus pr-2"></i> 
                            <span className="">Add Item</span>
                        </Link>
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
            </div>
        );
    }
}

export default Inventory;