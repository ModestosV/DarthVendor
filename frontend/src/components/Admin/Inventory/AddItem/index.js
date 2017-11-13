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
                this.setState({specs: ['ramSize', 'processorType', 'numCores', 'hardDriveSize', 'containsCamera', 'isTouch', 'batteryInfo', 'os', 'size']});
                break;
            case 'Tablet':
                this.setState({specs: ['ramSize', 'processorType', 'numCores', 'hardDriveSize', 'dx', 'dy', 'dz', 'os', 'batteryInfo', 'size', 'cameraInfo']});
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
            url: `${settings.API_ROOT}/addItemSpec`,
            withCredentials: true,
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

                        <div className="form-group row" key={index}>
                            <label htmlFor={name} className="col-sm-2 col-form-label"><strong>{name}</strong></label>
                            <div className="col-sm-10">
                                <input type="text" className="form-control" id={name}  name={name} onChange={(e) => this.handleSpecChange(e) }/>
                            </div>
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

        const {dispatch, history} = this.props;
        
        // Redirect if user is not logged in
        if (!localStorage.activeUser) {
            history.push('/login');
        } else {
            const activeUser = JSON.parse(localStorage.activeUser);

            if (activeUser.isAdmin === false) {
                // Redirect to merchant home page                
                history.push('/');
            }            
        }       
    }

    render() {
        const itemTypes = ['Desktop', 'Laptop', 'Tablet', 'Monitor Display'];
        const itemBasicSpecs = ['modelNumber', 'name', 'price', 'brandName', 'quantity', 'weight'];
        const itemSpecs = this.state.specs;
        const itemFields = itemBasicSpecs;
        itemFields.push.apply(itemFields, itemSpecs);

        return (
            <div>
                <Sidebar />
                <div className="container mt-4">
                
                    <div id="addItem">
                        <div className="mb-3">
                            <h1>Add New Item </h1>
                        </div>
                        <form id="addItemForm">
                            { this.typeSelect(itemTypes) }

                            { this.attributeFields(itemFields) }

                            <button
                                className="ui green button float-right mb-5"
                                onClick={() => this.confirmAddItem()}
                            >
                            <i className="fa fa-plus"></i> Add
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        )
    }
}

export default AddItem;
