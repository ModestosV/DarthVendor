import axios from 'axios';
import React, {Component} from 'react';
import settings from '../../../../config/settings';
import Sidebar from '../../Sidebar';


class AddItem extends Component {

    constructor(props) {
        super(props);

        this.state = {
            priceFormat: 'CAD',
            dimensionFormat: 'cm',
            sizeFormat: 'inch',
            ramFormat: 'GB',
            hardDriveFormat: 'GB',
            weightFormat: 'lbs',
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
                this.setState({specs: []});
                break;
        }
    }

    handleSpecChange(event) {
        this.setState({[event.target.name]: event.target.value});

    }

    handleForm() {

        let data = this.state;

        axios({
            method: 'post',
            url: `${settings.API_ROOT}/item`,
            data: data,
            headers: {
                Authorization: "Token " + JSON.parse(localStorage.activeUser).token
            }
        })
        .then(response => {
            console.log('item added');
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
        return (
            <div>
                <Sidebar />
                <div className="col-md-10 float-left col px-5 pl-md-2 pt-2 main">
                    <a href="#" data-target="#sidebar" data-toggle="collapse"><i className="fa fa-navicon fa-2x py-2 p-1"></i></a>
                    <div id="addItem">
                        <div>
                            <h1>Add New Item </h1>
                        </div>
                        <form>
                            {/* SELECT for type */}
                            <div className="input-group mb-3">
                                <select
                                    className="form-control"
                                    onChange={(e) => this.handleTypeChange(e)}
                                >
                                    <option value="">Choose type</option>
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
        )
    }
}

export default AddItem;
