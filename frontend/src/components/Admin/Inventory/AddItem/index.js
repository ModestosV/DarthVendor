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

    //set state on type select
    handleTypeChange(event) {
        this.setState({type: event.target.value});
        switch (event.target.value) {
            case 'Desktop':
                this.setState({specs: ['ramSize', 'processorType', 'numCores', 'hardDriveSize', 'dx', 'dy', 'dz']});
                break;
            case 'Laptop':
                this.setState({specs: ['ramSize', 'processorType', 'numCores', 'hardDriveSize', 'containCamera', 'isTouch', 'batteryInfo', 'os', 'size']});
                break;
            case 'Tablet':
<<<<<<< HEAD
                this.setState({specs: ['ramSize', 'ramFormat', 'processorType', 'numCores', 'hardDriveSize', 'hardDriveFormat', 'dx', 'dy', 'dz', 'dimensionFormat', 'os', 'batteryInfo', 'size', 'sizeFormat', 'cameraInfo']});
=======
                this.setState({specs: ['ramSize', 'processorType', 'numCores', 'hardDriveSize', 'dx', 'dy', 'dz', 'os', 'batteryInfo', 'size', 'cameraInfo']});
>>>>>>> 98b300a09056059e2d1b7008bdb550823968410a
                break;
            case 'Monitor Display':
                this.setState({specs: ['size']});
                break;
            default:
                this.setState({specs: []});
                break;
        }
    }

    // add attribute and value to the state
    handleSpecChange(event) {
        this.setState({[event.target.name]: event.target.value});
    }

    // add item post request
    confirmAddItem() {
        let data = this.state;

        axios({
            method: 'post',
            url: `${settings.API_ROOT}/item`,
            // withCredentials: true,
            data: data,
            headers: {
                Authorization: "Token " + JSON.parse(localStorage.activeUser).token
            }
        })
        .then(response => {
            console.log('item added');
            this.resetForm();
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

    // generate select input for item types
    typeSelect(itemTypes) {
        return (
            <div className="input-group mb-3">
                <select
                    id="selectItemTypes"
                    className="form-control"
                    onChange={(e) => this.handleTypeChange(e)}
                >
                    <option value="">Choose type</option>
                    { 
                        itemTypes.map((name,index) => {
                            return (
                                <option key={index} value={name}>
                                    {name}
                                </option>
                            );
                        })
                    }
                </select>
            </div>
        );
    }

    // generate input fields depending on selected item type
    attributeFields(itemFields) {
        if(this.state.type){
            return(
                itemFields.map((name,index) => {
                    return (
                        <div key={index} className="input-group mb-3">
                            <input
                                name={name}
                                type="text"
                                className="form-control"
                                placeholder={name}
                                onChange={(e) => this.handleSpecChange(e)}
                            />
                        </div>
                    );                                    
                })
            );
        }
    }

    resetForm() {
        document.getElementById("addItemForm").reset();
        this.forceUpdate();
    }

    componentWillMount() {
        console.log(localStorage);
    }

    render() {
        const itemTypes = ['Desktop', 'Laptop', 'Tablet', 'Monitor Display'];
<<<<<<< HEAD
        const itemBasicSpecs = ['modelNumber', 'name', 'price', 'priceFormat', 'brandName', 'quantity', 'weight', 'weightFormat'];
=======
        const itemBasicSpecs = ['modelNumber', 'name', 'price', 'brandName', 'quantity', 'weight'];
>>>>>>> 98b300a09056059e2d1b7008bdb550823968410a
        const itemSpecs = this.state.specs;
        const itemFields = itemBasicSpecs;
        itemFields.push.apply(itemFields, itemSpecs);
        
        return (
            <div>
                <Sidebar />
                <div className="pusher">
<<<<<<< HEAD

                    <div className="container p-0 mt-4">
                    <h1>Add New Item </h1>
                    </div>

                    <div id="addItem" className="mt-4 container">



                        <form className="row ui-form">
                            {/* SELECT for type */}
                            <div className="field mb-3 mr-3 ">
                                <select
                                    className="ui fluid dropdown"
                                    onChange={(e) => this.handleTypeChange(e)}
                                >
                                    <option value="">Default</option>
                                    {
                                        itemTypes.map((name,index) => {
                                            return (
                                                <option key={index} value={name}>
                                                    {name}
                                                </option>
                                            );
                                        })
                                    }
                                </select>
                            </div>

                            {/* Creates fields for every attributes  */}
                            {
                                itemFields.map((name,index) => {
                                    if(name.includes('Format')) {
                                        let unit = [];
                                        if(name == 'dimensionFormat') {
                                            unit = ['cm'];
                                        } else {
                                            if(name == 'sizeFormat') {
                                                unit = ['inch'];
                                            } else {
                                                if(name == 'ramFormat') {
                                                    unit = ['GB'];
                                                } else {
                                                    if(name == 'hardDriveFormat') {
                                                        unit = ['GB', 'TB'];
                                                    } else {
                                                        if(name == 'weightFormat') {
                                                            unit = ['lbs'];
                                                        } else {
                                                            unit = ['CAD'];
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                        return (
                                            <div key={index} className="field mb-3 mr-3 ">
                                                <select
                                                    className="ui fluid dropdown"
                                                    name={name}
                                                    onLoad={(e) => this.handleSpecChange(e)}
                                                    onChange={(e) => this.handleSpecChange(e)}
                                                >
                                                    {
                                                        unit.map((name2, index2) => {
                                                            return (
                                                                <option key={index2} value={name2}>
                                                                    {name2}
                                                                </option>
                                                            )
                                                        })
                                                    }
                                                </select>
                                            </div>
                                        );
                                    } else {
                                        return (

                                            <div key={index} className="mb-3 mr-3 ">
                                                <input
                                                    name={name}
                                                    className="form-control"
                                                    type="text"
                                                    placeholder={name}
                                                    onChange={(e) => this.handleSpecChange(e)}
                                                />
                                            </div>
                                        );
                                    }
                                })
                            }

                            <div className="max-width">
                                <button
                                    type="button"
                                    className="ui secondary button float-right mt-5"
                                    onClick={() => this.handleForm()}>
                                        Done
                                </button>
                            </div>

=======
                    <div id="addItem">
                        <div>
                            <h1>Add New Item </h1>
                        </div>
                        <form id="addItemForm">
                            { this.typeSelect(itemTypes) }

                            { this.attributeFields(itemFields) }
                            
                            <button
                                type="button"
                                className="btn btn-dark btn-block"
                                onClick={() => this.confirmAddItem()}
                            >
                                Add <i className="fa fa-plus"></i>
                            </button>
>>>>>>> 98b300a09056059e2d1b7008bdb550823968410a
                        </form>
                    </div>
                </div>
            </div>
        )
    }
}

export default AddItem;
