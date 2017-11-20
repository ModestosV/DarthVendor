import axios from 'axios';
import React, {Component} from 'react';
import {Link, HashRouter as Router, Route} from 'react-router-dom';
import settings from '../../../config/settings';
import Sidebar from '../Sidebar';
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';

import ReactModal from 'react-modal';

class Home extends Component {

    constructor(props) {
        super(props);
        this.state = {
            items:[],
            errorMsg: null,
            showModal: false,
            currentRow: ''
        };


        this.closeShowSpecsModal = this.closeShowSpecsModal.bind(this);
    }

    closeShowSpecsModal(){
        this.setState({showSpecsModal: false});
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
                history.push('/');
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
            this.setState({items});
            this.setState({catalog: items});
            this.setState({errorMsg});
            console.log(items);
        })
        .catch(error => {
         console.log(error);
         const errorMsg = "Oops, something went wrong while fetching items!";
         this.setState({errorMsg});
       })
    }

    showSpecs(row, index) {
        this.setState({currentRow: index});

        this.setState({showSpecsModal: true});
        this.setState({detailedItem: row}, () => this.getQuantity());
    }

    getQuantity() {
        axios({
            method: 'post',
            url:`${settings.API_ROOT}/getQuantity`,
            data: this.state.detailedItem,
            withCredentials: true
        }).then((result) => {
            this.setState({quantity: result.data.quantity})
        });
    }

    displayDetails(){
        if(this.state.detailedItem){

            return (
                <div className="row">
                    <div className="form-group col-sm-6">
                        <label htmlFor={name} className=""><strong>Quantity</strong></label>
                            <div className="">
                                {this.state.quantity}
                            </div>
                    </div>
                    {Object.keys(this.state.detailedItem).map((name,index) => {

                        if(typeof this.state.detailedItem[name] != 'object' && !name.includes('Format') && !name.includes('quantity')){
                            return (
                                <div className="form-group col-sm-6" key={index}>
                                    <label htmlFor={name} className="col-form-label"><strong>{name}</strong></label>
                                    <div>
                                        {this.state.detailedItem[name]}
                                    </div>
                                </div>
                            );
                        }
                    })
                    }
                </div>
            );
        }        
    
    }

    nextRow() {
        let max = this.state.catalog.length - 1;
        let nextRow = this.state.currentRow + 1;
        if(nextRow > max){
            nextRow = 0;
        }
        this.setState({currentRow: nextRow});
        this.setState({detailedItem: this.state.catalog[nextRow]},() => this.getQuantity());
    }

    previousRow() {
        let previousRow = this.state.currentRow - 1;
        if(previousRow < 0){
            previousRow = this.state.catalog.length - 1;
        }
        this.setState({currentRow: previousRow});
        this.setState({detailedItem: this.state.catalog[previousRow]},() => this.getQuantity());
    }

    render() {
        const self = this;
        function cellFormat(cell, row){
            return '<i class="glyphicon glyphicon-usd"></i> ' + cell;
        }

        function detailsFormat(cell, row, enumObject, index) {
            return <i onClick={() => self.showSpecs(row, index)} className="fa fa-info-circle fa-5" aria-hidden="true"></i>;
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
                <div className="container mb-5">
                    <link rel="stylesheet" href="https://npmcdn.com/react-bootstrap-table/dist/react-bootstrap-table-all.min.css"></link>
                    <h1> Inventory </h1>
                    { !!this.state.errorMsg && <div className="fa fa-warning errorMsg"> {this.state.errorMsg} </div> }
                    <br />
                    <BootstrapTable data={this.state.items} striped condensed hover search scrolling>
                        <TableHeaderColumn dataAlign="center" dataSort={false} width='40px' dataFormat={detailsFormat}> </TableHeaderColumn>
                        <TableHeaderColumn dataField="modelNumber" dataAlign="center" dataSort={true} dataFormat={cellFormat}>Model Number</TableHeaderColumn>
                        <TableHeaderColumn dataField="brandName" isKey={true} dataAlign="center" dataSort={true} dataFormat={cellFormat}>Brand Name</TableHeaderColumn>
                        <TableHeaderColumn dataField="type" dataAlign="center" dataSort={true} dataFormat={cellFormat}>Type</TableHeaderColumn>
                        <TableHeaderColumn dataField="weight" dataAlign="center" dataSort={true} dataFormat={cellFormat}>Weight (lbs)</TableHeaderColumn>
                        <TableHeaderColumn dataField="price" dataAlign="center" dataSort={true} sortFunc={sortFunc} dataFormat={cellFormat}>Price (CAD)</TableHeaderColumn>
                    </BootstrapTable>

                    {/* Modal for Spec item */}
                    <ReactModal isOpen={this.state.showSpecsModal} 
                            className={{base: 'modify--modal'}}>
                            <div>
                                <h1 className="float-left">
                                Details                                   
                                </h1>
                                <i className="remove icon float-right" onClick={this.closeShowSpecsModal}></i>
                                <i className="fa fa-arrow-circle-right float-right" aria-hidden="true" onClick={() => this.nextRow()}>Next</i>
                                <i className="fa fa-arrow-circle-left float-right" aria-hidden="true" onClick={() => this.previousRow()}>Previous</i> 
                            </div>
                            <div className="mt-50">
                                {this.displayDetails()}
                            </div>
                    </ReactModal>
                </div>
            </div>
        );
    }
}

export default Home
