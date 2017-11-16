import axios from 'axios';
import React, {Component} from 'react';
import {Link, withRouter} from 'react-router-dom';
import settings from '../../../../config/settings';
import Sidebar from '../../Sidebar';
import './updatelist.scss'


class UpdateList extends Component {

    constructor(props) {
        super(props);

        this.state = {
            items: [],
            addedItemIDs: [],
            currentlyEditing: false,
            deletedItemIDs: [],
            dirtySpecs: [],
            newSpecs: []
        }        
    }

    confirmUpdate() {
        swal({
            title: "Apply Updates?",
            text: "Are you sure you want to apply the updates?",            
            type: "warning",
            buttons: {
                confirm:true,
                cancel: true
            }            
          })
          .then((confirm) => {   
              if(confirm){
                console.log('updated');
                // window.location = '/'
                axios({
                    method: 'post',
                    url: `${settings.API_ROOT}/terminateEdit`,
                    data: {},
                    withCredentials: true
                }).then( result => {
                  swal({
                      text: "Changes applied!",
                      icon: "success",
                      button: "Ok",
                  })
                  .then(() => {
                    // this.props.history.push('/admin/update');
                    // window.location.href = '/';
                    // window.location.hash = "#/admin/update";
                    // location.reload()                      
                    window.location.reload();
                  })                  
                })
              }                
          });

    }

    cancelUpdate() {
        swal({
            title: "Cancel updates?",
            text: "Are you sure you want to cancel the updates?",            
            type: "warning",
            buttons: {
                confirm:true,
                cancel: true
            }            
          })
          .then((confirm) => {   
              if(confirm){
                  axios({
                      method: 'post',
                      url: `${settings.API_ROOT}/cancelEdit`,
                      withCredentials: true
                  })
                  .then(response => {                                        
                    swal("Canceled!", "The updates have been canceled", "success").then(
                      () => {
                        window.location.reload();
                      }
                    )


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
          });
    }

    getUpdateList() {
        axios({
            method:'get',
            url:`${settings.API_ROOT}/getEditState`,
            withCredentials: true
        })
        .then(results => {
            const errorMsg = null;
            let data = results.data;  
            
            // console.log(data);            
            // this.setState({errorMsg});

            if(data.currentlyEditing) {
                this.setState({
                    currentlyEditing: data.currentlyEditing,
                    dirtySpecs: data.dirtySpecs,
                    newSpecs: data.newSpecs,
                    addedItemIDs: data.addedItemIDs,
                    deletedItemIDs: data.deletedItemIDs
                });
            }            
        })
        .catch(error => {
         console.log(error);
         const errorMsg = "Oops, something went wrong while fetching items!";
         this.setState({errorMsg});
       })
    }

    // display list of updates
    displayUpdateList() {
      let display = [];
      let labelStyle = {
        fontWeight: 600
      };

      if (this.state.newSpecs.length === 0 && this.state.dirtySpecs.length === 0 && this.state.addedItemIDs.length === 0 && this.state.deletedItemIDs.length === 0) {
          return (                
            <div>
              No items changed.
            </div>  
          );
      }

      if (this.state.newSpecs.length > 0) {
          display.push(                
              <div>
                <label style={labelStyle}> News Specs </label>
                {
                  this.state.newSpecs.map((item, index) => {
                    return (
                      <li> {item.modelNumber} - {item.name} </li>
                    )
                  })
                }
              </div>  
          );
      }

      if (this.state.dirtySpecs.length > 0) {
          display.push(                
              <div>
                <label style={labelStyle}> Modify Specs </label>
                {
                  this.state.dirtySpecs.map((item, index) => {
                    return (
                      <li> {item.modelNumber} - {item.name} </li>
                    )
                  })
                }
              </div>  
          );
      } 

      if (this.state.addedItemIDs.length > 0) {
          display.push(                
              <div>
                <label style={labelStyle}> Add Items </label>
                {
                  this.state.addedItemIDs.map((item, index) => {
                    return (
                      <li> {item.itemSpec.modelNumber} - {item.itemSpec.name} </li>
                    )
                  })
                }
              </div>  
          );
      }  

      if (this.state.deletedItemIDs.length > 0) {
          display.push(                
              <div>
                <label style={labelStyle}> Delete Items </label>
                {
                  this.state.deletedItemIDs.map((item, index) => {
                    return (
                      <li> {item.itemSpec.modelNumber} - {item.itemSpec.name} </li>
                    )
                  })
                }
              </div>  
          );
      }                 

      return display;
    }

    displayButtons(){
        if(this.state.newSpecs.length > 0 || this.state.dirtySpecs.length > 0 || this.state.addedItemIDs.length > 0 || this.state.deletedItemIDs.length > 0 ){
            return (
                <div className="uow--buttons row">
                    <button className="col cancel ui button mx-3" onClick={() => {this.cancelUpdate()}}>Cancel</button>
                    <button className="col apply ui button mx-3" onClick={() => {this.confirmUpdate()}}>Apply</button>
                </div>
            )
        }
    }


    componentWillMount() {
        console.log(localStorage);
        this.getUpdateList();       
    }

    render() {
        return (
            <div className="col-sm-3 uow">
                <div className="uow--body">
                    <h2>Changes</h2>
                    {this.displayUpdateList() }
                    {this.displayButtons()}
                </div>
            </div>
        )
    }
}

export default withRouter(UpdateList);
