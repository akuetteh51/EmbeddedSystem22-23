import { StyleSheet, Text, View, TouchableNativeFeedback } from 'react-native';
import { WebView } from 'react-native-webview';
import { EvilIcons } from '@expo/vector-icons';
import {useRef} from 'react'
import {html} from './index.html.js'
import Signature from 'react-native-signature-canvas';

const ControlButton = ({icon, onPress, active})=>(
    <TouchableNativeFeedback onPress={onPress}>
        <View style={[styles.button, {backgroundColor: active? "#805":"#fff"}]}>
            <EvilIcons name={icon} size={30} color={ active? "#fff":"#aaa"}/>
        </View>
    </TouchableNativeFeedback>
)

const ActionButton = ({icon, onPress, title})=>(
  <TouchableNativeFeedback onPress={onPress}>
      <View style={{flexDirection:'row', justifyContent:'center', alignItems:'center', backgroundColor:'#229', height:45, paddingLeft:5, paddingRight:15, marginVertical:5, borderRadius:5}}>
          <EvilIcons name={icon} size={30} color="#fff"/>
          <Text style={{color:'#fff', marginLeft:5}}>{title}</Text>
      </View>
  </TouchableNativeFeedback>
)

export default function Drawing() {
  const canvasRef = useRef(null);
    const onPencilClick = ()=>{
        
    }
  
    const handleConfirm = () => {
      console.log("end");
      canvasRef.current.readSignature();
    }
  
    const undo = () => {
      canvasRef.current.undo();
    };

    const redo = () => {
      canvasRef.current.redo();
    };

    const handleClear = () => {
      canvasRef.current.clearSignature();
    };

    

  
    const eraseMode = () => {
      return
      canvasRef.current.erase();
    };
  
    const drawMode = () => {
      canvasRef.current.draw();
    };
  return (
    <View style={styles.container}>
      <View style={styles.top}>
        <View style={styles.tabControls}>
          <ControlButton active={true} onPress={()=>{}} icon="pencil"/>
          <ControlButton onPress={()=>{}} icon="image"/>
          <ControlButton onPress={()=>{}} icon="lock"/>
          <ControlButton onPress={()=>{}} icon="lock"/>
          <ControlButton onPress={()=>{}} icon="gear"/>
        </View>
        <View style={{flex:1}}>
          <View style={{justifyContent:'center', alignItems:'center'}}>
            <Text style={{color: "#fff", fontSize:18, fontStyle:'italic', marginVertical:5}}>👇👇👇 Draw here 👇👇👇</Text>
          </View>
          <View style={{flex:1, backgroundColor:'#444', overflow:'hidden', borderBottomLeftRadius:10, borderTopLeftRadius:10}}>
            <Signature
              ref={canvasRef}
              // handle when you click save button
              onOK={(img) => console.log(img)}
              onEmpty={() => console.log("empty")}

              // description text for signature
              descriptionText=""
              // clear button text
              // String, webview style for overwrite default style, all style: https://github.com/YanYuanFE/react-native-signature-canvas/blob/master/h5/css/signature-pad.css
              webStyle={`.m-signature-pad--footer
                .button {
                  display: none;
                }
                
                .m-signature-pad{
                  position:fixed;
                  top:10px;
                  bottom:10px;
                  right:10px;
                  left:10px;
                  height: auto;
                  width: auto;
                  padding:0px;
                  margin: 0px;
                }
                `
              }
              
              autoClear={true}
              imageType={"image/svg+xml"}
            />
          </View>
          <View style={{paddingHorizontal:10, flexDirection:'row'}}>
            <View style={styles.actionControls}>
              <ControlButton onPress={drawMode} icon="pencil"/>
              <ControlButton onPress={handleClear} icon="close-o"/>
              <ControlButton onPress={eraseMode} icon="lock"/>
            </View>
            <ActionButton icon="sc-telegram" title="Upload"/>
          </View>
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor:'#aaa',
    flexDirection: 'column'
  },
  top: {
    flex: 1,
    backgroundColor:'#aaa',
    flexDirection: 'row'
  },
  tabControls:{
      flex:1,
      maxWidth:55,
      height:'100%',
      backgroundColor:'transparent', 
      flexDirection:'column', 
      justifyContent:'center',
      alignItems:'center'
  },
  actionControls:{
    height: 50,
    flex:1,
    marginBottom:5,
    flexDirection:'row',
    justifyContent:'center'
  },
  button:{
      width:45,
      aspectRatio: 1,
      borderRadius: 5,
      backgroundColor: '#fff',
      alignItems:'center',
      justifyContent:'center',
      margin:5
  }
});
