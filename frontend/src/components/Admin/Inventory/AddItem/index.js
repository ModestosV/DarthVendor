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
        const itemTypes = ['Desktop', 'Laptop', 'Tablet', 'Monitor Display'];
        const itemBasicSpecs = ['modelNumber', 'name', 'price', 'priceFormat', 'brandName', 'quantity', 'weight', 'weightFormat'];
        const itemSpecs = this.state.specs;
        const itemFields = itemBasicSpecs;
        itemFields.push.apply(itemFields, itemSpecs);

        return (
            <div>
                <Sidebar />
                <div className="pusher">

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

                        </form>
                    </div>
                </div>
            </div>
        )
    }
}

export default AddItem;
