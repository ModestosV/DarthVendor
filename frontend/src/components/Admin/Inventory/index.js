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
            items:[],
            errorMsg: null,
            showModifyModal: false,
            showDeleteModal: false,
        };

        this.modifySpecs = this.modifySpecs.bind(this);
        this.openModifyModal = this.openModifyModal.bind(this);
        this.closeModifyModal = this.closeModifyModal.bind(this);
        this.openDeleteModal = this.openDeleteModal.bind(this);
        this.closeDeleteModal = this.closeDeleteModal.bind(this);
        this.deleteItems = this.deleteItems.bind(this);

    }

    componentWillMount() {
        const {dispatch, history} = this.props;
        
        // Redirect if user is not logged in
        if (!localStorage.activeUser) {
            history.push('/login');
        } else {
            const activeUser = JSON.parse(localStorage.activeUser);

            // Redirect to merchant home page                
            if (activeUser.adminPermission === false) {                
                history.push('/');
            }            
        }  
    }

    componentDidMount() {
        this.itemsList();     
    }

    openModifyModal () {
        this.setState({ showModifyModal: true });
    }

    closeModifyModal () {
        this.setState({ showModifyModal: false });
    }

    openDeleteModal () {
        this.setState({ showDeleteModal: true });
    }

    closeDeleteModal () {
        this.setState({ showDeleteModal: false });
    }

    itemsList() {
        return axios({
            method:'get',
            url:`${settings.API_ROOT}/inventory`,
            withCredentials: true
        })
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

    modifySpecs(row) {
        this.setState({item: row});
        this.openModifyModal();
    }

    deleteItems(row) {
        this.openDeleteModal();
        console.log("in delete Items")
    }

    

    render() {
        const self = this;

        function modifyCellFormat(cell, row){
            const modifyBtn = <i onClick={() => self.modifySpecs(row)} className="fa fa-pencil-square-o fa-5" aria-hidden="true"></i>;
            return modifyBtn;
        }

        function deleteCellFormat(cell, row){
            const deleteBtn = <i onClick={() => self.deleteItems(row)} className="fa fa-trash fa-5" aria-hidden="true"></i>;
            return deleteBtn;
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
                    <div className="mt-4">
                        <link rel="stylesheet" href="https://npmcdn.com/react-bootstrap-table/dist/react-bootstrap-table-all.min.css"></link>
                        <h1 className="m-0"> Inventory </h1>
                        { !!this.state.errorMsg && <div className="fa fa-warning errorMsg"> {this.state.errorMsg} </div> }
                        <br />
                        <Link to={`/admin/add`} className="list-group-item d-inline-block collapsed">
                            <i className="fa fa-plus pr-2"></i>
                            <span className="">Add Item</span>
                        </Link>

                        <BootstrapTable data={this.state.items} striped condensed hover pagination search scrolling >
                            <TableHeaderColumn dataField="modelNumber" dataAlign="center" dataSort={true} >Model Number</TableHeaderColumn>
                            <TableHeaderColumn dataField="brandName" isKey={true} dataAlign="center" dataSort={true} >Brand Name</TableHeaderColumn>
                            <TableHeaderColumn dataField="type" dataAlign="center" dataSort={true} >Type</TableHeaderColumn>
                            <TableHeaderColumn dataField="weight" dataAlign="center" dataSort={true} >Weight (lbs)</TableHeaderColumn>
                            <TableHeaderColumn dataField="price" dataAlign="center" dataSort={true} sortFunc={sortFunc} >Price (CAD)</TableHeaderColumn>
                            <TableHeaderColumn dataAlign="center" dataSort={false} width='40px' dataFormat={deleteCellFormat}> </TableHeaderColumn>
                            <TableHeaderColumn dataAlign="center" dataSort={false} width='40px' dataFormat={modifyCellFormat}> </TableHeaderColumn>
                        </BootstrapTable>
                    </div>
                </div>

                {/* Modal for Modify item */}
                <ReactModal isOpen={this.state.showModifyModal}>
                    <button onClick={this.closeModifyModal}>Cancel</button>
                    <ModifyItem item={this.state.item} closeModal={this.closeModifyModal}/>
                </ReactModal>

                {/* Modal for Delete item */}
                <ReactModal isOpen={this.state.showDeleteModal}>
                    <button onClick={this.closeDeleteModal}>Cancel</button>
                    <button onClick={this.closeDeleteModal}>Close Modal</button>
                    {/* <DeleteItem item={this.state.item} closeModal={this.closeDeleteModal}/> */}
                </ReactModal>

            </div>
        );
    }
}

export default Inventory;
