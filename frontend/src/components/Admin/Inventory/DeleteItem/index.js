import axios from 'axios';
import React, {Component} from 'react';
import settings from '../../../../config/settings';
import Sidebar from '../../Sidebar';

class DeleteItem extends Component {
    constructor(props) {
        super(props);
        this.state = {
            itemIDs: [],
            itemToDelete: ""
        }
    }
    // add deletions to UOW
    confirmDeletion() {
        //create object to post
        // let data = [];
        // data.push(this.props.item.modelNumber);
        // data.push(this.props.item.type);
        // data.push(this.state.itemToDelete);
        console.log(this.state.itemToDelete);
        let data = {
            modelNumber: this.props.item.modelNumber,
            serialNumber: this.state.itemToDelete,
            specType: this.props.item.type    
        }

        if(this.state.itemToDelete != ""){
            axios({
                method: 'post',
                url: `${settings.API_ROOT}/deleteItemID`,
                data: data,
                withCredentials: true
            }).then(result => {
                this.props.closeDeleteModal();
                window.location.reload();
            });


        }
    }

    // add deletions to UOW
    confirmDeleteSpec() {
        //create object to post
        // let data = [];
        // data.push(this.props.item.modelNumber);
        // data.push(this.props.item.type);
        // data.push(this.state.itemToDelete);
        let data = {
            modelNumber: this.props.item.modelNumber,
            specType: this.props.item.type    
        }

        axios({
            method: 'post',
            url: `${settings.API_ROOT}/deleteSpec`,
            data: data,
             withCredentials: true
        }).then(result => {
            this.props.closeDeleteModal();
            window.location.reload();
        });
    }

    // get item to delete
    componentWillMount() {
        // this.setState({item: this.props.item});

        axios({
            method: 'post',
            url: `${settings.API_ROOT}/getItemIDs`,
            data: this.props.item,
            withCredentials: true
        }).then(result => {
            this.setState({itemIDs: result.data});
            // let serials = [];
            // result.data.map((item,index) => {
            //     console.log(item)
            //     serials.push(item.serialNumber);
            // })
            // this.setState({itemIDs: serials});
        });
    }

    handleSelect(e) {
        this.setState({itemToDelete: e.target.value});
    }

    render() {
        const selectRowProp = {
            mode: 'radio',
            onSelect: this.selectItem
        };
        return (
            <div>
                <div>
                    <div className="mb-3">
                    Model Number: {this.props.item.modelNumber} <br/>
                    Type: {this.props.item.type}
                    </div>
                    <div className="form-group">
                        <select className="form-control" onChange={(e) => this.handleSelect(e)}>
                            <option value="">Select ID to delete</option>
                            {
                                this.state.itemIDs.map((item,index) => {
                                    return(
                                        <option 
                                            key={index} 
                                            value={item.serialNumber}
                                        >
                                            {item.isLocked? "(in a cart) ":""}{item.serialNumber}
                                        </option>
                                    )
                                })
                            }

                        </select>
                    </div>
                </div>
                <div className="mb-5">
                    <button  className="ui green button float-right"  onClick={() => {this.confirmDeletion()}}>Confirm</button>
                </div>

                    <button  className="ui green button float-right"  onClick={() => {this.confirmDeleteSpec()}}>Delete Specification</button>
            </div>
        )
    }
}
export default DeleteItem;
