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
            noError: false
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

    handleChange(event){
        this.setState({[event.target.name]: event.target.value});
    }

    handleModelNumberChange(event) {
        this.handleChange(event);

        if(/^[a-zA-Z0-9]*$/.test(event.target.value)) {
            this.setState({errorModelNumber: false});
            this.setState({noError: false});
        }else{
            this.setState({errorModelNumber: true});
            this.setState({noError: true});
        }
    }

    handleWeightChange(event) {
        this.handleChange(event);

        if(/^([0-9]\d*(.\d+)?|)$/.test(event.target.value)) {
            this.setState({errorWeight: false});
            this.setState({noError: false});
        }else{
            this.setState({errorWeight: true});
            this.setState({noError: true});
        }
    }

    handlePriceChange(event) {
        this.handleChange(event);

        if(/^([0-9]\d*(.\d+)?|)$/.test(event.target.value)) {
            this.setState({errorPrice: false});
            this.setState({noError: false});
        }else{
            this.setState({errorPrice: true});
            this.setState({noError: true});
        }        
    }

    handleSizeChange(event) {
        this.handleChange(event);

        if(/^([0-9]\d*(.\d+)?|)$/.test(event.target.value)) {
            this.setState({errorSize: false});
            this.setState({noError: false});
        }else{
            this.setState({errorSize: true});
            this.setState({noError: true});
        }        
    }

    handleRamSizeChange(event) {
        this.handleChange(event);

        if(/^[0-9]*$/.test(event.target.value)) {
            this.setState({errorRamSize: false});
            this.setState({noError: false});
        }else{
            this.setState({errorRamSize: true});
            this.setState({noError: true});
        }          
    }

    handleNumCoresChange(event) {
        this.handleChange(event);

        if(/^[0-9]*$/.test(event.target.value)) {
            this.setState({errorNumCores: false});
            this.setState({noError: false});
        }else{
            this.setState({errorNumCores: true});
            this.setState({noError: true});
        }          
    }

    handleHDSizeChange(event) {
        this.handleChange(event);

        if(/^([0-9]\d*(.\d+)?|)$/.test(event.target.value)) {
            this.setState({errorHDSize: false});
            this.setState({noError: false});
        }else{
            this.setState({errorHDSize: true});
            this.setState({noError: true});            
        }          
    }

    handleDXChange(event) {
        this.handleChange(event);

        if(/^([0-9]\d*(.\d+)?|)$/.test(event.target.value)) {
            this.setState({errorDX: false});
            this.setState({noError: false});
        }else{
            this.setState({errorDX: true});
            this.setState({noError: true});
        }          
    }

    handleDYChange(event) {
        this.handleChange(event);

        if(/^([0-9]\d*(.\d+)?|)$/.test(event.target.value)) {
            this.setState({errorDY: false});
            this.setState({noError: false});
        }else{
            this.setState({errorDY: true});
            this.setState({noError: true});
        }          
    }

    handleDZChange(event) {
        this.handleChange(event);

        if(/^([0-9]\d*(.\d+)?|)$/.test(event.target.value)) {
            this.setState({errorDZ: false});
            this.setState({noError: false});
        }else{
            this.setState({errorDZ: true});
            this.setState({noError: true});
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
            data: data
        })
        .then(response => {
            swal({
                text: "Item Spec Added!",
                icon: "success",
                button: "Ok",
            })
            .then(() => {                                
                window.location.href = '/';
                window.location.hash = "#/admin/update";
                location.reload()
            })            
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
        let input = null;

        let modelNumber, weight, price, size, ramSize, numCores, hardDriveSize, dx, dy, dz;
        modelNumber = weight = price = size = ramSize = numCores= hardDriveSize = dy = dx = dz = "form-control";

        let modelNumberMsg, weightMsg, priceMsg, sizeMsg, ramSizeMsg, numCoresMsg, hardDriveSizeMsg, dxMsg, dyMsg, dzMsg;
        modelNumberMsg  = weightMsg = priceMsg = sizeMsg = ramSizeMsg = numCoresMsg = hardDriveSizeMsg = dxMsg = dyMsg = dzMsg = "list-group-item hidden";

        let errorCSS = "form-control input--error";
        let errorMsgCSS = "list-group-item";

        if (this.state.errorModelNumber){
            modelNumber = errorCSS;
            modelNumberMsg = errorMsgCSS;
        }
        if (this.state.errorWeight) {
            weight = errorCSS;
            weightMsg = errorMsgCSS;
        }
        if (this.state.errorPrice) {
            price = errorCSS;
            priceMsg = errorMsgCSS;
        }
        if (this.state.errorSize) {
            size = errorCSS;
            sizeMsg = errorMsgCSS;
        }
        if (this.state.errorRamSize) {
            ramSize = errorCSS;
            ramSizeMsg = errorMsgCSS;
        }
        if(this.state.errorNumCores) {
            numCores = errorCSS;
            numCoresMsg = errorMsgCSS;
        }
        if(this.state.errorHDSize) {
            hardDriveSize = errorCSS;
            hardDriveSizeMsg = errorMsgCSS;
        }
        if(this.state.errorDX) {
            dx = errorCSS;
            dxMsg = errorMsgCSS;
        }
        if(this.state.errorDY) {
            dy = errorCSS;
            dyMsg = errorMsgCSS;
        }
        if(this.state.errorDZ) {
            dz = errorCSS;
            dzMsg = errorMsgCSS;
        }

        if(this.state.type){
            return(
                itemFields.map((name,index) => {
                    if(name === "modelNumber") {
                        input = <input type="text"
                                    className={modelNumber}
                                    id={name}
                                    name={name}
                                    onChange={ (e) => this.handleModelNumberChange(e) }/>
                    } else if (name === "weight") {
                        input = <input type="text"
                                    className={weight}
                                    id={name}
                                    name={name}
                                    onChange={ (e) => this.handleWeightChange(e) }/>
                    } else if (name === "price") {
                        input = <input type="text"
                                    className={price}
                                    id={name}
                                    name={name}
                                    onChange={ (e) => this.handlePriceChange(e) }/>
                    } else if (name === "size") {
                        input = <input type="text"
                                    className={size}
                                    id={name}
                                    name={name}
                                    onChange={ (e) => this.handleSizeChange(e) }/>
                    } else if (name === "ramSize") {
                        input = <input type="text"
                                    className={ramSize}
                                    id={name}
                                    name={name}
                                    onChange={ (e) => this.handleRamSizeChange(e) }/>
                    } else if (name === "numCores") {
                        input = <input type="text"
                                    className={numCores}
                                    id={name}
                                    name={name}
                                    onChange={ (e) => this.handleNumCoresChange(e) }/>
                    } else if (name === "hardDriveSize") {
                        input = <input type="text"
                                    className={hardDriveSize}
                                    id={name}
                                    name={name}
                                    onChange={ (e) => this.handleHDSizeChange(e) }/>
                    } else if (name === "dx") {
                        input = <input type="text"
                                    className={dx}
                                    id={name}
                                    name={name}
                                    onChange={ (e) => this.handleDXChange(e) }/>
                    } else if (name === "dy") {
                        input = <input type="text"
                                    className={dy}
                                    id={name}
                                    name={name}
                                    onChange={ (e) => this.handleDYChange(e) }/>
                    } else if (name === "dz") {
                        input = <input type="text"
                                    className={dz}
                                    id={name}
                                    name={name}
                                    onChange={ (e) => this.handleDZChange(e) }/>
                    } else {
                        input = <input type="text"
                                    className="form-control"
                                    id={name}
                                    name={name}
                                    onChange={ (e) => this.handleChange(e) }/>
                    }
                    return (
                        <div className="form-group row" key={index}>
                            <label htmlFor={name} className="col-sm-2 col-form-label"><strong>{name}</strong></label>
                            <div className="col-sm-10">
                                <div className="error--message mb-2 mt-0">
                                    <ul className="list-group">
                                        {name === "modelNumber" && <li className={modelNumberMsg}>Invalid Model Number</li>}
                                        {name === "weight" && <li className={weightMsg}>Invalid Weight </li>}
                                        {name === "price" && <li className={priceMsg}>Invalid Price </li>}
                                        {name === "size" && <li className={sizeMsg}>Invalid Size </li>}
                                        {name === "ramSize" && <li className={ramSizeMsg}>Invalid RAM Size </li>}
                                        {name === "numCores" && <li className={numCoresMsg}>Invalid Number of Cores </li>}
                                        {name === "hardDriveSize" && <li className={hardDriveSizeMsg}>Invalid HD Size </li>}
                                        {name === "dx" && <li className={dxMsg}>Invalid DX </li>}
                                        {name === "dy" && <li className={dyMsg}>Invalid DY </li>}
                                        {name === "dz" && <li className={dzMsg}>Invalid DZ </li>}
                                    </ul>
                                </div>
                                {input}
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
        const itemBasicSpecs = ['modelNumber', 'name', 'price', 'brandName', 'weight'];
        const itemSpecs = this.state.specs;
        const itemFields = itemBasicSpecs;
        itemFields.push.apply(itemFields, itemSpecs);

        return (
            <div>
                <Sidebar />
                <div className="container mt-4">
                
                    <div id="addItem">
                        <div className="mb-3">
                            <h1>Add Item Spec</h1>
                        </div>
                        <form id="addItemForm">
                            { this.typeSelect(itemTypes) }
                            { this.attributeFields(itemFields) }

                            {this.state.noError == true && 
                                <button className="ui green button disabled float-right mb-5">
                                    <i className="fa fa-plus"></i> Add
                                </button>
                            }

                            {this.state.noError == false && 
                                <button className="ui green button float-right mb-5" onClick={() => this.confirmAddItem()}>
                                    <i className="fa fa-plus"></i> Add
                                </button>
                            }
                        </form>
                    </div>
                </div>
            </div>
        )
    }
}

export default AddItem;
