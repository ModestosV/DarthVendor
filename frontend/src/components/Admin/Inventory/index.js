import axios from 'axios';
import React, {Component} from 'react';
import {Link, HashRouter as Router, Route} from 'react-router-dom';
import settings from '../../../config/settings';
import Sidebar from '../Sidebar';
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';

class Inventory extends Component {

    componentWillMount() {  
        const {history} = this.props;      
        console.log(localStorage);
        
        if (!localStorage.activeUser) {
            history.push('/login');
        }
    }

    render() {

var items = [{
      id: 1,
      name: "Item name 1",
      price: 50
  },{
      id: 2,
      name: "Item name 2",
      price: 100
  }
];
        return (
            <div>
                <Sidebar />
                <div className="col-md-10 float-left col px-5 pl-md-2 pt-2 main">
                    <a href="#" data-target="#sidebar" data-toggle="collapse"><i className="fa fa-navicon fa-2x py-2 p-1"></i></a>
                    <h1> Inventory </h1>
                    <BootstrapTable data={items} striped={true} hover={true}>
                        <TableHeaderColumn dataField="id" isKey={true} dataAlign="center" dataSort={true}>Product ID</TableHeaderColumn>
                        <TableHeaderColumn dataField="name" dataSort={true}>Product Name</TableHeaderColumn>
                        <TableHeaderColumn dataField="price" dataSort={true}>Product Price</TableHeaderColumn>
                    </BootstrapTable>
                  </div>
                  <Link to={`/inventory/add`} className="list-group-item d-inline-block collapsed"><i className="fa fa-plus"></i> <span className="d-none d-md-inline">Add Item</span></Link>
            </div>
        );
    }
}

export default Inventory;