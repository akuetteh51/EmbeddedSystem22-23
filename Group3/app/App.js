import { StatusBar } from 'expo-status-bar';
import { StyleSheet, View } from 'react-native';
import Drawing from './src/Drawing';
import constants from 'expo-constants';

export default function App() {
  return (
    <View style={[styles.container,{marginTop: constants.statusBarHeight}]}>
      <StatusBar style="auto" />
      <Drawing/>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor:'#fff'
  },
});
