import axios from 'axios';
import React, {Component} from 'react';
import swal from 'sweetalert';
import settings from '../../config/settings';
import './Inventory.scss';


class AddItem extends Component {    

    constructor(props) {
        super(props);

        this.state = {
            priceFormat: 'CAD',
            dimensionFormat: 'cm',
            sizeFormat: 'inch',
            ramFormat: 'GB',
            hardDriveFormat: 'GB',
            weightFormat: 'lbs'
        }
    }

    handleTypeChange(event) {
        this.setState({type: event.target.value});
        switch (event.target.value) {
            case 'Desktop':
                this.setState({specs: ['ramSize', 'ramFormat', 'processorType', 'numCores', 'hardDriveSize', 'hardDriveFormat', 'dx', 'dy', 'dz', 'dimensionFormat']});
                break;
            case 'Laptop':
                this.setState({specs: ['ramSize', 'ramFormat', 'processorType', 'numCores', 'hardDriveSize', 'hardDriveFormat', 'containCamera', 'isTouch', 'batteryInfo', 'os', 'size', 'sizeFormat']});
                break;
            case 'Tablet':
                this.setState({specs: ['ramSize', 'ramFormat', 'processorType', 'numCores', 'hardDriveSize', 'hardDriveFormat', 'dx', 'dy', 'dz', 'dimensionFormat', 'os', 'batteryInfo', 'size', 'sizeFormat', 'cameraInfo']});
                break;
            case 'Television':
                this.setState({specs: ['tvType', 'dimensionFormat', 'dx', 'dy', 'dz']});
                break;
            case 'Monitor Display':
                this.setState({specs: ['size','sizeFormat']});
                break;
            default:
                break;
        }
    }

    handleSpecChange(event) {
        event.target.name = event.target.name == 'RAM' ? 'ram' : event.target.name;
        this.setState({[event.target.name]: event.target.value});
        
    }

    handleForm() {        
        // const {dispatch, history} = this.props;

        let dataItem = {
            'type': this.state.type,
            'modelNumber': this.state.modelNumber, 
            'price': this.state.price,
            'quantity': this.state.quantity
        };

        let dataType;
        switch (this.state.type) {
            case 'Desktop':
                dataType = {
                    'processor': this.state.processor,
                    'RAM': this.state.ram
                };
                break;
            case 'Laptop':
                dataType = {
                    'size': this.state.size,
                    'touch': this.state.touch
                };
                break;
            default:
                break;
        }

        Object.assign(dataItem,dataType);
        console.log(this.state);
    }

    componentWillMount() {        
        console.log(localStorage);
    }

    render() {
        const itemTypes = ['Desktop', 'Laptop', 'Tablet', 'Television', 'Monitor Display'];
        const itemBasicSpecs = ['modelNumber', 'price', 'priceFormat', 'brandName', 'quantity', 'weight', 'weightFormat'];
        const itemSpecs = this.state.specs;
        const itemFields = itemBasicSpecs;
        itemFields.push.apply(itemFields, itemSpecs);
        console.log(this.state);
        console.log(itemFields);
        return (
            <div className="container">                
                <div className="row">                    
                    <div className="col-md-4" />
                    <div className="col-md-4" style={{marginTop: '30%'}}>
                        <div id="addItem">
                            <div>
                                <h1> Add New Item </h1>
                            </div>
                            <form>
                                {/* SELECT for type */}
                                <div className="input-group mb-3">
                                    <select 
                                        className="form-control"
                                        onChange={(e) => this.handleTypeChange(e)}
                                    >
                                        <option value=""></option>
                                        { itemTypes.map((name,index) => {
                                        return (
                                            <option 
                                                key={ index }
                                                value={ name }
                                            >{ name }
                                            </option>);
                                        })}
                                    </select>
                                </div>

                                {/* creates fields for every attributes  */}
                                { itemFields.map((name,index) => {
                                        if(name.includes('Format')){
                                            let unit = [];
                                            if(name == 'dimensionFormat'){ unit = ['cm'];}
                                            else{if(name == 'sizeFormat'){ unit = ['inch'];}
                                                else{if(name == 'ramFormat'){ unit = ['GB'];}
                                                    else{if(name == 'hardDriveFormat'){ unit = ['GB', 'TB'];}
                                                        else{if(name == 'weightFormat'){ unit = ['lbs'];}
                                                            else{unit = ['CAD'];}}}}}
                                            return (
                                                <div key={ index } className="input-group mb-3">
                                                    <select name={ name } onLoad={(e) => this.handleSpecChange(e)} onChange={(e) => this.handleSpecChange(e)}>
                                                        
                                                        { unit.map((name2, index2) => {
                                                            return (
                                                                <option key={ index2 } value={ name2 }>{ name2 }</option>)
                                                        })}
                                                    </select>
                                                    
                                                </div>);
                                        }else {
                                            return (
                                                <div key={ index } className="input-group mb-3">
                                                    <input 
                                                        name={ name }
                                                        type="text" 
                                                        className="form-control"                             
                                                        placeholder={ name }
                                                        onChange={(e) => this.handleSpecChange(e)}
                                                    />
                                                </div>);
                                        }
                                })}
                                <button 
                                    type="button" 
                                    className="btn btn-dark btn-block"
                                    onClick={() => this.handleForm()}>
                                        Add <i className="fa fa-plus"></i>
                                </button>                    
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default AddItem;