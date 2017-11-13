import axios from 'axios';
import React, {Component} from 'react';
import {HashRouter as Router, Route} from 'react-router-dom';
import settings from '../../../config/settings';
import Navigation from '../Navigation';
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';
import './Catalog.scss';


class Catalog extends Component {

    constructor(props) {
        super(props);
        this.state = {
            items:[],
            errorMsg: null,
            showModal: false
        };
    }

    componentWillMount() {
        const {history} = this.props;
        console.log(localStorage);
    }

    componentDidMount() {
        this.getCatalog();
    }

    getCatalog() {
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

    renderItems(items) {
        return(
            <div className="ui five column grid">
            {
                items.map((item,index) => {
                console.log(item.name);
                    return (
                        <div className="column" key={index}>
                            <div className="ui fluid card">
                                <div className="content">
                                    <a className="header">{item.name}</a>
                                </div>
                            </div>
                        </div>
                    );
                })
            }
            </div>
        );
    }

    addToCart(row) {
        if(localStorage.activeUser){
            console.log("lock :" + row );
            let data = row;

            axios({
                method: 'post',
                url: `${settings.API_ROOT}/addToCart`,
                data: data,
                withCredentials: true
            })
            .then(response => {
                swal({
                    text: "Item added to cart!",
                    icon: "success",
                    button: "Ok",
                });
            })
            .catch(error => {
                console.log(error);
                swal({
                    title: "Woops!",
                    text: "Something went wrong!",
                    icon: "error",
                    button: "Ok",
                });
            })
        } else {
            swal("Oops!", "You need to login to add item to cart", "error");
        }

    }
    render() {
        const self = this;

        function sortFunc(a, b, order) {
            if (order === 'desc') {
                return a.price - b.price;
            } else {
                return b.price - a.price;
            }
        }

        function addToCartFormat(cell, row) {
            return <i onClick={() => self.addToCart(row)} className="fa fa-shopping-cart fa-5" aria-hidden="true"></i>;
        }
       // const items = this.state.items;

        return (
            <div>
                <Navigation />

                {/* { items.map((item)=> <li>{ item.name }</li> )} */}
                <link rel="stylesheet" href="https://npmcdn.com/react-bootstrap-table/dist/react-bootstrap-table-all.min.css"></link>
                <div className="mt-5">
                    <div className="row">
                        <div className="col-sm-9">
                            <BootstrapTable data={this.state.items} condensed search scrolling className="item--table">
                            <TableHeaderColumn dataField="modelNumber" dataAlign="center" dataSort={true} >Model Number</TableHeaderColumn>
                            <TableHeaderColumn dataField="brandName" isKey={true} dataAlign="center" dataSort={true} >Brand Name</TableHeaderColumn>
                            <TableHeaderColumn dataField="type" dataAlign="center" dataSort={true} >Type</TableHeaderColumn>
                            <TableHeaderColumn dataField="weight" dataAlign="center" dataSort={true} >Weight (lbs)</TableHeaderColumn>
                            <TableHeaderColumn dataField="price" dataAlign="center" dataSort={true} sortFunc={sortFunc} >Price (CAD)</TableHeaderColumn>
                            <TableHeaderColumn dataAlign="center" dataSort={false} width='40px' dataFormat={addToCartFormat}> </TableHeaderColumn>
                            </BootstrapTable>
                        </div>
                        {/* {this.renderItems(items)} */}
                    </div>
                </div>

            </div>

        )
    }
}

export default Catalog;
