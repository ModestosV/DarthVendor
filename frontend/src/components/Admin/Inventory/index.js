import axios from 'axios';
import React, {Component} from 'react';
import ReactModal from 'react-modal';
import {Link, HashRouter as Router, Route} from 'react-router-dom';
import settings from '../../../config/settings';
import Sidebar from '../Sidebar';
import ModifyItem from './ModifyItem';
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';

class Inventory extends Component {

    constructor(props) {
        super(props);
        this.state = {
            items: [],
            errorMsg: null,
            showModal: false
        };

        this.showSpecs = this.showSpecs.bind(this);
        this.openModal = this.openModal.bind(this);
        this.closeModal = this.closeModal.bind(this);

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

    openModal () {
        this.setState({ showModal: true });
    }
    
    closeModal () {
        this.setState({ showModal: false });
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

    showSpecs(row) {
        this.setState({item: row});
        this.openModal();
        console.log(this.state);
    }

    render() {
        function cellFormat(cell, row){
            return '<i className="glyphicon glyphicon-usd"></i> ' + cell;
        }

        function sortFunc(a, b, order) {   
            if (order === 'desc') {
                return a.price - b.price;
            } else {
                return b.price - a.price;
            }
        }

        function displaySpecs(row){
            console.log('aa')
            
        }

        const options = { 
            onRowClick: this.showSpecs
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

                        <BootstrapTable data={this.state.items} options={options} striped condensed hover pagination search scrolling >
                            <TableHeaderColumn dataField="modelNumber" dataAlign="center" dataSort={true} dataFormat={cellFormat}>Model Number</TableHeaderColumn>                        
                            <TableHeaderColumn dataField="brandName" isKey={true} dataAlign="center" dataSort={true} dataFormat={cellFormat}>Brand Name</TableHeaderColumn>                        
                            <TableHeaderColumn dataField="type" dataAlign="center" dataSort={true} dataFormat={cellFormat}>Type</TableHeaderColumn>
                            <TableHeaderColumn dataField="weight" dataAlign="center" dataSort={true} dataFormat={cellFormat}>Weight (lbs)</TableHeaderColumn>
                            <TableHeaderColumn dataField="price" dataAlign="center" dataSort={true} sortFunc={sortFunc} dataFormat={cellFormat}>Price (CAD)</TableHeaderColumn>                      
                            <TableHeaderColumn dataField="quantity" dataAlign="center" dataSort={true} dataFormat={cellFormat}>Quantity</TableHeaderColumn>                        
                        </BootstrapTable>
                    </div>    
                </div>
                <ReactModal 
                isOpen={this.state.showModal}
                contentLabel="Minimal Modal Example"
                >
                    <button onClick={this.closeModal}>Close Modal</button>
                    <ModifyItem item={this.state.item} closeModal={this.closeModal}/>
                </ReactModal>
            </div>
        );
    }
}

export default Inventory;