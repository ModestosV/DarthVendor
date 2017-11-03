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
    //     return axios.get(`${settings.API_ROOT}/inventory`)
    //     .then(results => {
    //         const errorMsg = null;
    //         const items = results.data.map(item => item);
    //         this.setState({items});
    //         this.setState({errorMsg});
    //         console.log(items);
    //     })
    //     .catch(error => {
    //      console.log(error);
    //      const errorMsg = "Oops, something went wrong while fetching items!";
    //      this.setState({errorMsg});
    //    })
    }

    showSpecs(row, columnIndex, rowIndex) {
        console.log(columnIndex);
        this.setState({item: row});
        this.openModal();
        console.log(this.state);
    }

    createDeleteBtn(onClick) {
        console.log('in createdelete')
        return(
            <button onClick={e => handleDelete(onClick)}>Delete</button>
        );
    }

    handleDelete(onClick){
        console.log('in handle');
        onClick();
    }

    render() {
        
        function cellFormat(cell, row){
            return '<div onClick=hey()></div>' +cell;
        }

        function deleteCellFormat(cell, row){
            
            return '<i class="fa fa-trash fa-5" aria-hidden="true"></i>';
            
            }
            
            function modifyCellFormat(cell, row){
            
            return '<i class="fa fa-pencil-square-o fa-5" aria-hidden="true"></i>';
            
            }

        function sortFunc(a, b, order) {   
            if (order === 'desc') {
                return a.price - b.price;
            } else {
                return b.price - a.price;
            }
        }

        const options = { 
            onRowClick: this.showSpecs,
            deleteBtn: this.createDeleteBtn
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
                            <TableHeaderColumn dataField="modelNumber" dataAlign="center" dataSort={true} >Model Number</TableHeaderColumn>                        
                            <TableHeaderColumn dataField="brandName" isKey={true} dataAlign="center" dataSort={true} >Brand Name</TableHeaderColumn>                        
                            <TableHeaderColumn dataField="type" dataAlign="center" dataSort={true} >Type</TableHeaderColumn>
                            <TableHeaderColumn dataField="weight" dataAlign="center" dataSort={true} >Weight (lbs)</TableHeaderColumn>
                            <TableHeaderColumn dataField="price" dataAlign="center" dataSort={true} sortFunc={sortFunc} >Price (CAD)</TableHeaderColumn>                      
                            <TableHeaderColumn dataField="quantity" dataAlign="center" dataSort={true} >Quantity</TableHeaderColumn>                        
                            <TableHeaderColumn dataAlign="center" dataSort={false} width='40px' dataFormat={deleteCellFormat}> </TableHeaderColumn>
                            <TableHeaderColumn dataAlign="center" dataSort={false} width='40px' dataFormat={modifyCellFormat}> </TableHeaderColumn>
                        </BootstrapTable>
                    </div>    
                </div>

                {/* Modal for Modify item */}
                <ReactModal isOpen={this.state.showModal}>
                    <button onClick={this.closeModal}>Close Modal</button>
                    <ModifyItem item={this.state.item} closeModal={this.closeModal}/>
                </ReactModal>

            </div>
        );
    }
}

export default Inventory;