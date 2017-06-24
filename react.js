import React, { Component } from 'react';
import {
  AppRegistry,
  StyleSheet,
  View,
  Button,
  TouchableWithoutFeedback,
  Text,
} from 'react-native';

class MyButton extends Component {
  render() {
    return (
      <View style={styles.button}>
        <TouchableWithoutFeedback
          onPress={this.props.onPress}
          style={styles.button}>
          <Text style={styles.buttonText}> {this.props.status} </Text>
        </TouchableWithoutFeedback>
      </View>
    );
  }
}

export default class Board extends Component {
  constructor(props) {
    super(props);
    this.state = { board: Array(9).fill(' '), turn: false };
  }
  
  checkWinner(board) {
    // Looks for the winner. The ugliest piece of my code
    let copyOfBoard = board.slice();
    let case1 = (copyOfBoard[0] == copyOfBoard[1] && copyOfBoard[1] == copyOfBoard[2] && copyOfBoard[0] != " ");
    let case2 = (copyOfBoard[3] == copyOfBoard[4] && copyOfBoard[4] == copyOfBoard[5] && copyOfBoard[3] != " ");
    let case3 = (copyOfBoard[6] == copyOfBoard[7] && copyOfBoard[7] == copyOfBoard[8] && copyOfBoard[6] != " ");
    let case4 = (copyOfBoard[0] == copyOfBoard[4] && copyOfBoard[4] == copyOfBoard[8] && copyOfBoard[0] != " ");
    let case5 = (copyOfBoard[2] == copyOfBoard[4] && copyOfBoard[4] == copyOfBoard[6] && copyOfBoard[2] != " "); 
    let case6 = (copyOfBoard[0] == copyOfBoard[3] && copyOfBoard[3] == copyOfBoard[6] && copyOfBoard[0] != " ");
    let case7 = (copyOfBoard[1] == copyOfBoard[4] && copyOfBoard[4] == copyOfBoard[5] && copyOfBoard[1] != " ");
    let case8 = (copyOfBoard[2] == copyOfBoard[5] && copyOfBoard[5] == copyOfBoard[8] && copyOfBoard[2] != " ");
    
    if (case1 || case2 || case3 || case4 || case5 || case6 || case7 || case8) {
      alert((copyOfBoard[0].toUpperCase() + " won!"));
      return true;
    } 
  }
  
  _onPressButton(num) {
    // Looks for amount of empty squares
    let counter = 0;
    for (let i = 0; i < 9; i += 1) {
      if (this.state.board[i] == ' ') {
        counter += 1;
      }
    }
    
    // If they are not left
    if (!(counter < 1)) {
      let status = this.state.board[num];
      if (status == ' ') {
        this.setState(prev_state => {
          let new_board = prev_state.board.slice();
          let turn = prev_state.turn;
          if (turn) {
            new_board[num] = 'x';
          }
          if (!turn) {
            new_board[num] = 'o';
          }
          if (this.checkWinner(new_board)) {
            new_board = Array(9).fill(' ');
          }
          return { board: new_board, turn: !prev_state.turn };
        });
      }
    } else {
      if (this.checkWinner(this.state.board)) {
        this.setState(prev_state => {
          return { board: Array(9).fill(' '), turn: !prev_state.turn };
        });
      }
    }
  }
  render() {
    return (
      <View style={{ flex: 1, marginTop: 20 }}>

        <View
          style={{
            flexDirection: 'row',
            justifyContent: 'flex-start',
            alignItems: 'flex-start',
            width: 30,
          }}>

          <MyButton
            onPress={() => this._onPressButton(0)}
            status={this.state.board[0]}
          />
          <MyButton
            onPress={() => this._onPressButton(1)}
            status={this.state.board[1]}
          />
          <MyButton
            onPress={() => this._onPressButton(2)}
            status={this.state.board[2]}
          />

        </View>

        <View
          style={{
            flexDirection: 'row',
            justifyContent: 'flex-start',
            alignItems: 'flex-start',
            width: 30,
          }}>

          <MyButton
            onPress={() => this._onPressButton(3)}
            status={this.state.board[3]}
          />
          <MyButton
            onPress={() => this._onPressButton(4)}
            status={this.state.board[4]}
          />
          <MyButton
            onPress={() => this._onPressButton(5)}
            status={this.state.board[5]}
          />

        </View>

        <View
          style={{
            flexDirection: 'row',
            justifyContent: 'flex-start',
            alignItems: 'flex-start',
            width: 30,
          }}>

          <MyButton
            onPress={() => this._onPressButton(6)}
            status={this.state.board[6]}
          />
          <MyButton
            onPress={() => this._onPressButton(7)}
            status={this.state.board[7]}
          />
          <MyButton
            onPress={() => this._onPressButton(8)}
            status={this.state.board[8]}
          />
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  button: {
    marginBottom: 5,
    marginTop: 8,
    marginRight: 3,
    width: 105.3,
    height: 105.3,
    backgroundColor: '#2196F3',
  },
  buttonText: {
    fontSize: 60,
    padding: 22,
    color: 'white',
    fontWeight: 'bold',
  },
});

// skip this line if using Create React Native App
AppRegistry.registerComponent('Board', () => Board);
