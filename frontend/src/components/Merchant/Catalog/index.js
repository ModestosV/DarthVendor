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
            items:[
            {'name':"Razer Desktop"},
            {'name':"Dell Desktop"},
            {'name':"MacBook Desktop"},
            {'name':"ASUS Desktop"},
            {'name':"Good Desktop"},
            {'name':"Bad Desktop"},
            {'name':"Cool Desktop"}],
            errorMsg: null,
            showModal: false
        };
        console.log(this.state.items);
    }

    componentWillMount() {  
        const {history} = this.props;      
        console.log(localStorage);
    }

    componentDidMount() {
        //this.getCatalog();
    }

    getCatalog() {
        return axios.get(`${settings.API_ROOT}/catalog`)
        .then(results => {
            //const errorMsg = null;
            // const items = results.data.map(item => item);
            // this.setState({items});
            //this.setState({errorMsg});
            //console.log(items);
        })
        .catch(error => {
         console.log(error);
         //const errorMsg = "Oops, something went wrong while fetching items!";
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
    
    
    render() {
        const columns = [['name','Name'],['price','Price']];
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
       // const items = this.state.items;

        return (
            
            <div>
                <Navigation />

                {/* { items.map((item)=> <li>{ item.name }</li> )} */}

                <div className="container mt-5">
                    <div className="row">
                        <div className="col-sm-3">
                        
                        </div>

                        <div className="col-sm-9">
                        <BootstrapTable data={this.state.items} condensed hover search scrolling className="item--table">            
                    <TableHeaderColumn dataField="name" isKey={true} dataAlign="center" dataSort={true} dataFormat={cellFormat}>Items</TableHeaderColumn>                          
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