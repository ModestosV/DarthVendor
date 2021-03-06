import axios from 'axios';
import React, {Component} from 'react';
import {HashRouter as Router, Route} from 'react-router-dom';
import settings from '../../../config/settings';
import Navigation from '../Navigation';
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';
import './Return.scss';


class Return extends Component {

    constructor(props) {
        super(props);
        this.state = {
            items:[],
            returnItems:[],
            errorMsg: null,
            showModal: false
        };

        this.selectItem = this.selectItem.bind(this);
    }

    componentWillMount() {
        const {history} = this.props;
        console.log(localStorage);

        if (!localStorage.activeUser) {
            history.push('/login');
        } else {
            const activeUser = JSON.parse(localStorage.activeUser);

            // Making sure user does not have admin permission
            if (activeUser.isAdmin === true) {
                // Redirect to admin home page
                history.push('/admin/');
            }
        }
    }

    componentDidMount() {
        this.getPurchaseCollection();
    }

    // get list of purchased items
    getPurchaseCollection() {
        return axios({
            method: 'get',
            url: `${settings.API_ROOT}/getPurchaseCollection`,
            withCredentials: true
        })
        .then(results => {
            const errorMsg = null;
            const items = results.data.map((item,index) => {
                item.name = item.spec.name;
                return item;
            })
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

    returnItems() {
        let data = this.state.returnItems;

        axios({
            method: 'post',
            url: `${settings.API_ROOT}/returnItems`,
            withCredentials: true,
            data: data,
            headers: {
                Authorization: "Token " + JSON.parse(localStorage.activeUser).token
            }
        })
        .then(response => {
            console.log('item added');
            window.location.reload()
        })
        .catch(error => {
            console.log(error);
            swal({
                title: "Woops!",
                text: "Something went wrong!",
                ilcon: "error",
                button: "Ok",
            });
        })
    }

    renderItems(items) {
        return(
            <div className="ui five column grid">
            {
                items.map((item,index) => {
                    console.log(item)
                    return (
                        <div className="column" key={index}>
                            <div className="ui fluid card">
                                <div className="content">
                                    <a className="header">{item.spec.name}</a>
                                </div>
                            </div>
                        </div>
                    );
                })
            }
            </div>
        );
    }

    selectItem(row, isSelected, e) {
        if(isSelected) {
            this.setState({
                returnItems: [...this.state.returnItems, row]
            })
        }else{
            this.setState({
                returnItems: this.state.returnItems.filter(item => item.modelNumber != row.modelNumber)
            })
        }
    }

    render() {
        const columns = [['name','Name'],['price','Price']];

        const selectRowProp = {
            mode: 'checkbox',
            onSelect: this.selectItem
        };

        function cellFormat(cell, row){
            return '<i class="glyphicon glyphicon-usd"></i> ' + cell;
        }

        return (
            <div>
                <Navigation />
                <div className="container mt-5">
                    <div className="row">
                        <div className="col-sm-3">
                        </div>
                        <h1 className="ml-4">Purchase History</h1>
        
                        <div className="col-sm-9">
                        <div>
                        <BootstrapTable data={this.state.items} selectRow={selectRowProp} condensed hover search scrolling className="item--table">
                            <TableHeaderColumn dataField="name" dataAlign="center" dataSort={true} dataFormat={cellFormat}>Item Name</TableHeaderColumn>
                            <TableHeaderColumn dataField="serialNumber" isKey={true} dataAlign="center" dataSort={true} dataFormat={cellFormat}>Serial Number</TableHeaderColumn>
                        </BootstrapTable>
                        </div>
                        </div>
                    </div>
                    <div className="row">
                        <div className="col-sm-3"></div>
                        <div className="col-sm-9">
                            <button className="ui green button mt-3" onClick={() => this.returnItems()}>Return Items</button>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default Return;
