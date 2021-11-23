import React from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import styled from "styled-components";

import { Container, Button } from "react-bootstrap";

import Header from './components/Header';
import HomePageContent from './components/HomePageContent';
import Footer from './components/Footer';

const AppContainer = styled(Container)`
  padding: 0px 0px;
  margin: 0px 0px;
`;

function App() {
  return (
    <div className="App">
      <AppContainer fluid>
			  <Header/>
      </AppContainer>
      <AppContainer fluid>
				<main><HomePageContent></HomePageContent></main>
			</AppContainer>
      <AppContainer fluid>
				<Footer/>
			</AppContainer>
    </div>
  );
}

export default App;
