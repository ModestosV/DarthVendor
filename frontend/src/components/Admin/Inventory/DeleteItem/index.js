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
        if(this.state.itemToDelete != ""){
            axios({
                method: 'post',
                url: `${settings.API_ROOT}/deleteItemID`,
                data: this.state.itemToDelete,
                withCredentials: true
            }).then(result => {
                this.props.closeDeleteModal();
            });
    
            
        }  
    }

    // display specs of selected item
    displaySpecs() {

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
            let serials = [];
            result.data.map((item,index) => {
                serials.push(item.serialNumber);
            })
            this.setState({itemIDs: serials});
        });
    }

    handleSelect(e) {
        this.setState({itemToDelete: e.target.value});
    }

    render() {
        console.log(this.state.itemToDelete);
        const selectRowProp = {
            mode: 'radio',
            onSelect: this.selectItem
        };
        return (
            <div>
                <div>
                    Model Number: {this.props.item.modelNumber} <br/>
                    Type: {this.props.item.type}
                    <div className="form-group">
                        <select className="form-control" onChange={(e) => this.handleSelect(e)}>
                            <option value="">Select ID to delete</option>
                            {
                                this.state.itemIDs.map((serial,index) => {
                                    return(
                                        <option key={index} value={serial}>{serial}</option>
                                    )
                                })
                            }
                            
                        </select>
                    </div>
                </div>

                <div className="mb-5">
                    <button  className="ui green button float-right"  onClick={() => {this.confirmDeletion()}}>Confirm</button>
                </div>

            </div>


        )
    }
}
export default DeleteItem;
