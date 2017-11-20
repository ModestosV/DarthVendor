import axios from 'axios';
import React, {Component} from 'react';
import {HashRouter as Router, Route} from 'react-router-dom';
import {Form, Checkbox} from 'semantic-ui-react';
import settings from '../../../config/settings';
import Navigation from '../Navigation';
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';
import './Catalog.scss';
import Slider from 'react-rangeslider';

import ReactModal from 'react-modal';


class Catalog extends Component {

    constructor(props) {
        super(props);
        this.state = {
            items:[],
            errorMsg: null,
            showSpecsModal: false,
            priceSlider: '',
            maxPrice: '',
            typeFilter: '',
            sizeFilter: '',
            brandFilter: [],
            quantity: 0,
            processorTypeFilter: [],
            currentRow: ''
        };
        this.handleOnChange = this.handleOnChange.bind(this);
        this.handleChangeComplete = this.handleChangeComplete.bind(this);
        this.renderFilterBrand = this.renderFilterBrand.bind(this);
        this.closeShowSpecsModal = this.closeShowSpecsModal.bind(this);
        // this.handleFilter = this.handleFilter.bind(this);
    }

    componentWillMount() {
        const {history} = this.props;
        console.log(localStorage);

        if (localStorage.activeUser) {
            const activeUser = JSON.parse(localStorage.activeUser);

            if (activeUser.isAdmin === true) {
                // Redirect to admin home page                
                history.push('/admin');
            }             
        }

    }

    componentDidMount() {
        this.getCatalog();
    }

    closeShowSpecsModal(){
        this.setState({showSpecsModal: false});
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
                                
                let text = "Something went wrong!";
                // Out of stock / full cart error
                if (error.request.status === 412) {
                    let response = JSON.parse(error.request.response);                                                           
                    text = response.message;
                } 

                swal({
                    title: "Woops!",
                    text: text,
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
                    max={Number(this.state.maxPrice)}
                    value={Number(priceSlider)}
                    orientation="horizontal"
                    onChange={this.handleOnChange}
                    onChangeComplete={this.handleChangeComplete}
                />
                <div className='float-right'>$ {priceSlider}</div>

            </div>
        )
    }

    renderFilterType() {
        const itemTypes = ['Desktop', 'Laptop', 'Tablet', 'Monitor'];
        return(
            <div className="grouped fields mt-5">
                <h4>Type</h4>
                <Form>
                {
                    itemTypes.map((type,index) => {
                        return (
                            <div>  
                                <Form.Field key={index}>
                                    <Checkbox label={type} value={type} checked={this.state.typeFilter == type} onChange={(event, data) => this.handleFilterType(data)}/>
                                </Form.Field>
                            </div>
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
                <div className="grouped fields mt-3">
                    <h4>Brand</h4>
                    <Form>
                        {
                            this.state.brandsList.map((brand,index) => {
                                return(
                                    <div>
                                    <Form.Field key={index}>
                                        <Checkbox label={brand} value={brand} onChange={(event, data) => this.handleFilterBrand(data)}/>
                                    </Form.Field>
                                    </div>
                                )
                            })
                        }
                    </Form>
                </div>
            )
        }
    }

    renderFilterSpecific() {
        if(this.state.typeFilter == 'Monitor'){
            return (
                <div className="grouped fields mt-3">
                    <h4>Size</h4>
                    <Form>
                        <div>
                        <Form.Field>
                            <Checkbox label="<=24 inches" value="1" checked={this.state.sizeFilter == '1'} onChange={(event, data) => this.handleFilterSize(data)}/>
                        </Form.Field>
                        </div>
                        <div>
                        <Form.Field>
                            <Checkbox label="<=27 inches" value="2" checked={this.state.sizeFilter == '2'} onChange={(event, data) => this.handleFilterSize(data)}/>
                        </Form.Field>
                        </div>
                        <div>
                        <Form.Field>
                            <Checkbox label=">27 inches" value="3" checked={this.state.sizeFilter == '3'} onChange={(event, data) => this.handleFilterSize(data)}/>
                        </Form.Field>
                        </div>

                    </Form>
                </div>
            )
        }
        if(this.state.typeFilter == 'Desktop'){
            let processors = [];
            this.state.items.map((item,index) => {
                if(item.type == 'DESKTOP'){
                    if(!processors.includes(item.processorType)){
                        processors.push(item.processorType);
                    }
                }
            })
            return (
                <div className="grouped fields mt-3">
                    <h4>Processor Type</h4>
                    <Form>
                        {
                            processors.map((type,index) => {
                                return(
                                    <div>
                                    <Form.Field key={index}>
                                        <Checkbox label={type} value={type} onChange={(event, data) => this.handleFilterProcessorType(data)}/>
                                    </Form.Field>
                                    </div>
                                )
                            })
                        }
                    </Form>
                </div>
            )
        }
    }

    handleFilterProcessorType(data) {
        if(data.checked){
            let b = this.state.processorTypeFilter;
            b.push(data.value)
            this.setState({processorTypeFilter: b},() => this.handleFilter())
        }else{
            let b = this.state.processorTypeFilter;
            b = b.filter(type => type != data.value);
            this.setState({processorTypeFilter: b},() => this.handleFilter());
        }
    }

    handleFilterSize(data) {
        if(data.checked){
            this.setState({sizeFilter: data.value},() => this.handleFilter());
        } else {
            this.setState({sizeFilter: ''},() => this.handleFilter())
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
            //filter by processor type
            if(this.state.processorTypeFilter.length != 0){
                let f = [];
                this.state.processorTypeFilter.map((type,index) => {
                    f= [...f, filteredItems.filter(item => item.processorType == type)];
                })
                let f2 = [];
                f.map((items,index) => {
                    items.map((item,index2) => {
                        f2.push(item);
                    })

                })
                filteredItems = f2;
            }
        }
        if(this.state.typeFilter == 'Laptop'){
            filteredItems = filteredItems.filter(item => item.type == 'LAPTOP')

        }
        if(this.state.typeFilter == 'Tablet'){
            filteredItems = filteredItems.filter(item => item.type == 'TABLET')
        }
        if(this.state.typeFilter == 'Monitor'){
            filteredItems = filteredItems.filter(item => item.type == 'MONITOR')
            //filterby size
            if(this.state.sizeFilter != ''){
                if(this.state.sizeFilter == '1'){
                    filteredItems = filteredItems.filter(item => item.size <= 24);
                }
                if(this.state.sizeFilter == '2'){
                    filteredItems = filteredItems.filter(item => item.size <= 27);
                }
                if(this.state.sizeFilter == '3'){
                    filteredItems = filteredItems.filter(item => item.size > 27);
                }
            }
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

    showSpecs(row, index) {
        this.setState({currentRow: index});

        this.setState({showSpecsModal: true});
        this.setState({detailedItem: row}, () => this.getQuantity());
    }

    getQuantity(){
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

        function detailsFormat(cell, row, enumObject, index) {
            return <i onClick={() => self.showSpecs(row, index)} className="fa fa-info-circle fa-5" aria-hidden="true"></i>;
        }

        return (

            <div>
                <Navigation />
                <div className="container mt-5">
                    <div className="row">
                        <div className="col-sm-2 mb-5">
                        <h2>Filters</h2>

                            {this.renderFilterPrice()}
                            {this.renderFilterType()}
                            {this.renderFilterBrand()}
                            {this.renderFilterSpecific()}
                            {/* <button onClick={() => this.handleFilter()}>Apply</button> */}

                        </div>

                        <div className="col-sm-10">
                            {/* { items.map((item)=> <li>{ item.name }</li> )} */}
                            <link rel="stylesheet" href="https://npmcdn.com/react-bootstrap-table/dist/react-bootstrap-table-all.min.css"></link>

                            <BootstrapTable data={this.state.catalog} condensed search scrolling className="catalog--table">
                            <TableHeaderColumn dataAlign="center" dataSort={false} width='40px' dataFormat={detailsFormat}> </TableHeaderColumn>
                            <TableHeaderColumn dataField="name" dataAlign="center" dataSort={true} >Name</TableHeaderColumn>
                            <TableHeaderColumn dataField="modelNumber" dataAlign="center" dataSort={true} >Model Number</TableHeaderColumn>
                            <TableHeaderColumn dataField="brandName" isKey={true} dataAlign="center" dataSort={true} >Brand Name</TableHeaderColumn>
                            <TableHeaderColumn dataField="type" dataAlign="center" dataSort={true} >Type</TableHeaderColumn>
                            <TableHeaderColumn dataField="weight" dataAlign="center" dataSort={true} >Weight (lbs)</TableHeaderColumn>
                            <TableHeaderColumn dataField="price" dataAlign="center" dataSort={true} sortFunc={sortFunc} >Price (CAD)</TableHeaderColumn>
                            <TableHeaderColumn dataAlign="center" dataSort={false} width='40px' dataFormat={addToCartFormat}> </TableHeaderColumn>
                            </BootstrapTable>

                        </div>

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
                            <div className="mt-50 container">
                                {this.displayDetails()}
                            </div>
                        </ReactModal>
                    </div>
                </div>
            </div>

        )
    }
}

export default Catalog;
