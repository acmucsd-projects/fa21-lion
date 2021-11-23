import React from "react";
import {Container, Row, Col, Button} from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import styled from "styled-components";

const HeaderRight = styled(Col)`
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    padding: 0px;
    position: absolute;
    right: 48px;
    flex: none;
    flex-grow: 0;
    margin: 0px 16px;
`;

const HeaderButton = styled(Button)`
    background-color: MediumTurquoise;
    border: none;
    position: static;
    flex: none;
    flex-grow: 0;
    margin: 0px 16px;
`;

const Logo = styled(Button)`
    position: static;
    left: 48px;
    flex: none;
    flex-grow: 0;
    margin: 0px 16px;
`;

function Header(props) {

	return (
		<div style={{'background-color': 'Black', 'padding': '36px', 'align-items': 'center', 'display': 'flex'}}>
            <Col style={{'align-items': 'center', 'display': 'flex'}}>
                <Logo>Logo</Logo>
            </Col>
            <HeaderRight>
                <Col>
                    <HeaderButton>Testing</HeaderButton>
                </Col>
                <Col>
                    <HeaderButton>Testing</HeaderButton>
                </Col>
            </HeaderRight>
		</div>
	);
}

export default Header;