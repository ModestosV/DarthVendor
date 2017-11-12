import axios from 'axios';
import React, {Component} from 'react';
import ReactModal from 'react-modal';
import {Link, HashRouter as Router, Route} from 'react-router-dom';
import settings from '../../../config/settings';
import Sidebar from '../Sidebar';
import ModifyItem from './ModifyItem';
import UpdateList from './UpdateList';
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';
import DeleteItem from './DeleteItem';

class Inventory extends Component {
    constructor(props) {
        super(props);
        this.state = {
            item: [],
            // items:[{'modelNumber':'ZZZZZZZ',
            // 'quantity':46,
            // 'name':'Razer Desktop',
            // 'weight':15.0,
            // 'weightFormat':'lbs',
            // 'price':2299.99,
            // 'priceFormat':'CAD',
            // 'brandName':'RAZER',
            // 'type':'Desktop',
            // 'ramSize':16,
            // 'ramFormat':'GB',
            // 'processorType':'INTEL',
            // 'numCores':4,
            // 'hardDriveSize':2,
            // 'hardDriveFormat':'TB',
            // 'dx':15,
            // 'dy':30,
            // 'dz':1,
            // 'dimensionFormat':'INCH'}],
            items:[],
            errorMsg: null,
            showModifyModal: false,
            showDeleteModal: false,
            currentlyEditing: false,
            editedSpecs: [],
            newItemIDs: [],
            deletedItemIDs:[]
        };
        this.modifySpecs = this.modifySpecs.bind(this);
        this.openModifyModal = this.openModifyModal.bind(this);
        this.closeModifyModal = this.closeModifyModal.bind(this);
        this.openDeleteModal = this.openDeleteModal.bind(this);
        this.closeDeleteModal = this.closeDeleteModal.bind(this);
        this.deleteItems = this.deleteItems.bind(this);
    }
    componentWillMount() {
        const {history} = this.props;
        if (!localStorage.activeUser) {
            history.push('/login');
        }
    }

    componentWillMount() {
        const {dispatch, history} = this.props;

        // Redirect if user is not logged in
        if (!localStorage.activeUser) {
            history.push('/login');
        } else {
            const activeUser = JSON.parse(localStorage.activeUser);

            // Redirect to merchant home page
            if (activeUser.isAdmin === false) {
                history.push('/');
            }
        }
    }

    componentWillMount() {
        axios({
            method: 'get',
            url: `${settings.API_ROOT}/getEditState`,
            withCredentials: true
        }).then(results => {
            var data = results.data;
            if(data.currentlyEditing) {
                this.setState({
                    currentlyEditing: data.currentlyEditing,
                    editedSpecs: data.editedSpecs,
                    newItemIDs: data.newItemIDs,
                    deletedItemIDs: data.deletedItemIDs
                });
            } else {
                axios({
                    method: 'post',
                    data: {},
                    url: `${settings.API_ROOT}/initiateEdit`,
                    withCredentials: true
                }).then( result => {
                    this.setState({currentlyEditing: true})
                });
            }
        })
    }

    componentDidMount() {
        this.getItemsList();
        this.getUpdatedItemList();
    }

    openModifyModal () {
        this.setState({showModifyModal: true});
    }

    closeModifyModal () {
        this.setState({showModifyModal: false});
    }

    openDeleteModal () {
        this.setState({showDeleteModal: true});
    }

    closeDeleteModal () {
        this.setState({showDeleteModal: false});
    }

    getItemsList() {
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

    getUpdatedItemList() {
        //    return axios({
    //         method:'get',
    //         url:`${settings.API_ROOT}/inventory`,
    //         withCredentials: true
    //     })
    //     .then(results => {
    //         const errorMsg = null;
    //         const items = results.data.map(item => item);
    //         const abc ="abc";
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

    modifySpecs(row) {
        this.setState({item: row});
        this.openModifyModal();
    }

    createDeleteButton(onClick) {
        console.log('created delete');
        return (
            <i class="fa fa-trash fa-5" onClick={e => handleDelete()} aria-hidden="true"></i>
        )
    }

    deleteItems(row) {
        this.openDeleteModal();
        this.setState({item: row});
    }

    terminateEdit() {
        axios({
            method: 'post',
            url: `${settings.API_ROOT}/terminateEdit`,
            data: {},
            withCredentials: true
        }).then( result => {
            this.props.history.push('/')
        })
    }

    render() {

        const self = this;

        function modifyCellFormat(cell, row){
            return <i onClick={() => self.modifySpecs(row)} className="fa fa-pencil-square-o fa-5" aria-hidden="true"></i>;
        }

        function deleteCellFormat(cell, row){
            return <i onClick={() => self.deleteItems(row)} className="fa fa-trash fa-5" aria-hidden="true"></i>;
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
                        <button type='button' onClick={() => this.terminateEdit()} className="list-group-item d-inline-block collapsed">Confirm Changes</button>
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
                    <DeleteItem item={this.state.item} closeDeleteModal={this.closeDeleteModal}/>
                </ReactModal>
                <UpdateList />
            </div>
        );
    }
}

export default Inventory;
