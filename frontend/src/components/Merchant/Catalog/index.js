import axios from 'axios';
import React, {Component} from 'react';
import {HashRouter as Router, Route} from 'react-router-dom';
import {Form, Checkbox} from 'semantic-ui-react';
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
            typeFilter: '',        
            brandFilter: [],
        };
        this.handleOnChange = this.handleOnChange.bind(this);
        this.handleChangeComplete = this.handleChangeComplete.bind(this);
        this.renderFilterBrand = this.renderFilterBrand.bind(this);
        // this.handleFilter = this.handleFilter.bind(this);
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
            this.setState({catalog: items});
            this.getMaxPrice();
            this.getBrands();
            this.setState({errorMsg});
        })
        .catch(error => {
         console.log(error);
         const errorMsg = "Oops, something went wrong while fetching items!";
         this.setState({errorMsg});
       })
    }

    getMaxPrice(){
        
        let max = 0;
        this.state.items.map((item,index) => {
            if (max < parseInt(item.price)){
                max = item.price;
            }
        })
        this.state.maxPrice = max;
        this.state.priceSlider = max;
    }

    getBrands() { 
        let brands = [];
        this.state.items.map((item,index) => {
            if(!brands.includes(item.brandName)){
                brands.push(item.brandName);
            }
        })
        this.setState({brandsList: brands});
    }

    handleOnChange(value){
        this.setState({
          priceSlider: value
        })
    };

    handleChangeComplete(){
        this.handleFilter();
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

    renderFilterPrice() {
        const priceSlider  = this.state.priceSlider;
        return(
            <div className="grouped fields">

                <h4>Price</h4>
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
        )
    }

    renderFilterType() {
        const itemTypes = ['Desktop', 'Laptop', 'Tablet', 'Monitor'];
        return(
            <div className="grouped fields">

                <h4>Type</h4>
                <Form>
                {
                    itemTypes.map((type,index) => {
                        return (
                            <Form.Field key={index}>
                                <Checkbox label={type} value={type} checked={this.state.typeFilter == type} onChange={(event, data) => this.handleFilterType(data)}/>
                            </Form.Field>
                        )
                    })
                }
                </Form>
                
            </div>
        )
    }

    renderFilterBrand() {
        if(this.state.brandsList){
            return (
                <div className="grouped fields">
                    <h4>Brand</h4>
                    <Form>
                        {
                            this.state.brandsList.map((brand,index) => {
                                return(
                                    <Form.Field key={index}>
                                        <Checkbox label={brand} value={brand} onChange={(event, data) => this.handleFilterBrand(data)}/>    
                                    </Form.Field>
                                )
                            })
                        }
                    </Form>
                </div>
            )
        }                           
    }
    
    handleFilterBrand(data) {
        if(data.checked){
            let b = this.state.brandFilter;
            b.push(data.value)
            this.setState({brandFilter: b},() => this.handleFilter())
        }else{
            let b = this.state.brandFilter;
            b = b.filter(brand => brand != data.value);
            this.setState({brandFilter: b},() => this.handleFilter());
        }
    }

    handleFilterType(data) {
        if(data.checked){
            this.setState({typeFilter: data.label},() => this.handleFilter());
        }else{
            this.setState({typeFilter: ''},() => this.handleFilter());
        }
        
        
    }

    handleFilter(){
        //start filter by price
        let filteredItems = this.state.items.filter(item => item.price <= this.state.priceSlider);

        // filter by type
        if(this.state.typeFilter == 'Desktop'){
            filteredItems = filteredItems.filter(item => item.type == 'DESKTOP')
        }
        if(this.state.typeFilter == 'Laptop'){
            filteredItems = filteredItems.filter(item => item.type == 'LAPTOP')
        }
        if(this.state.typeFilter == 'Tablet'){
            filteredItems = filteredItems.filter(item => item.type == 'TABLET')
        }
        if(this.state.typeFilter == 'Monitor'){
            filteredItems = filteredItems.filter(item => item.type == 'MONITOR')
        }

        //filter by brand
        if(this.state.brandFilter.length != 0){
            let f = [];
            this.state.brandFilter.map((brand,index) => {
                f= [...f, filteredItems.filter(item => item.brandName == brand)];
                // f.push(filteredItems.filter(item => item.brandName == brand));
            })
            let f2 = [];
            f.map((items,index) => {
                items.map((item,index2) => {
                    console.log(item)
                    f2.push(item);
                })
                
            })
            filteredItems = f2;

        }

        this.setState({catalog: filteredItems});         
        
    }

    test() {
        console.log('aaa')
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
        function onRowClick() {
            self.test();
        }

        var options = {
            onRowClick: onRowClick()
        }

        return (
            
            <div>
                <Navigation />
                <div className="container mt-5">
                    <div className="row">
                        <div className="col-sm-2">
                        <h2>Filters</h2>

                            {this.renderFilterPrice()}
                            {this.renderFilterType()}
                            {this.renderFilterBrand()}
                            {/* <button onClick={() => this.handleFilter()}>Apply</button> */}

                        </div>

                        <div className="col-sm-10">
                            {/* { items.map((item)=> <li>{ item.name }</li> )} */}
                            <link rel="stylesheet" href="https://npmcdn.com/react-bootstrap-table/dist/react-bootstrap-table-all.min.css"></link>

                            <BootstrapTable data={this.state.catalog} option={options} condensed search scrolling className="catalog--table">
                            <TableHeaderColumn dataField="name" dataAlign="center" dataSort={true} >Name</TableHeaderColumn>
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
