import axios from 'axios';
import React, {Component} from 'react';
import {HashRouter as Router, Route} from 'react-router-dom';
import settings from '../../../config/settings';
import Navigation from '../Navigation';
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';
import './Catalog.scss';
import Slider from 'react-rangeslider';


class Catalog extends Component {    

    constructor(props) {
        super(props);
        this.state = {
            items:[],
            errorMsg: null,
            showModal: false,
            priceSlider: '',
            maxPrice: '',
        };
        this.handleOnChange = this.handleOnChange.bind(this);
        this.handleChangeComplete = this.handleChangeComplete.bind(this);
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
            this.setState({payload: items});
            this.getMaxPrice();
            this.setState({errorMsg});
            console.log(items);
        })
        .catch(error => {
         console.log(error);
         const errorMsg = "Oops, something went wrong while fetching items!";
         this.setState({errorMsg});
       })
    }

    getMaxPrice(){
        let temp = this.state.items;
        let max = 0;
        for(let i = 0; i < temp.length; i++){
            if (max < parseInt(temp[i].price)){
                max = temp[i].price;
            }
        }
        this.state.maxPrice = max;
        this.state.priceSlider = max;
    }

    handleOnChange(value){
        this.setState({
          priceSlider: value
        })
    };

    handleChangeComplete(){
        let price = this.state.priceSlider;
        if(price === ""){
            this.setState({payload: this.state.items});
        } else {
            let filteredItems = this.state.items.filter(item => item.price < price);
            this.setState({payload: filteredItems});         
        }
    }

    
    addToCart(row) {
        if(localStorage.activeUser){
            console.log("lock :" + row );
            let data = row;
    
            axios({
                method: 'post',
                url: `${settings.API_ROOT}/cart`,
                data: data,
                headers: {
                    Authorization: "Token " + JSON.parse(localStorage.activeUser).token
                }
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
        const priceSlider  = this.state.priceSlider;
        
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

        return (
            <div>
                <Navigation />
                <div className="container mt-5">
                    <div className="row">
                        <div className="col-sm-2">
                        <h2>Filters</h2>

                            <div className="ui form mb-2">
                                <div className="grouped fields">

                                <h4>Prices</h4>

                                    <Slider
                                        min={1}
                                        max={this.state.maxPrice}
                                        value={priceSlider}
                                        orientation="horizontal"
                                        onChange={this.handleOnChange}
                                        onChangeComplete={this.handleChangeComplete}
                                    />

                                    <div className='float-right'>{priceSlider}</div>

                                </div>
                            </div>

                        </div>

                        <div className="col-sm-10">
                            {/* { items.map((item)=> <li>{ item.name }</li> )} */}
                            <link rel="stylesheet" href="https://npmcdn.com/react-bootstrap-table/dist/react-bootstrap-table-all.min.css"></link>

                            <BootstrapTable data={this.state.payload} condensed search scrolling className="item--table">
                            <TableHeaderColumn dataField="modelNumber" dataAlign="center" dataSort={true} >Model Number</TableHeaderColumn>
                            <TableHeaderColumn dataField="brandName" isKey={true} dataAlign="center" dataSort={true} >Brand Name</TableHeaderColumn>
                            <TableHeaderColumn dataField="type" dataAlign="center" dataSort={true} >Type</TableHeaderColumn>
                            <TableHeaderColumn dataField="weight" dataAlign="center" dataSort={true} >Weight (lbs)</TableHeaderColumn>
                            <TableHeaderColumn dataField="price" dataAlign="center" dataSort={true} sortFunc={sortFunc} >Price (CAD)</TableHeaderColumn>
                            <TableHeaderColumn dataAlign="center" dataSort={false} width='40px' dataFormat={addToCartFormat}> </TableHeaderColumn>
                            </BootstrapTable>                      
    
                        </div>

                    </div>
                </div>
   

            </div>
     
        )
    }
}

export default Catalog;