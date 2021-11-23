import React from "react";
import { Container, Row, Col, Button } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import styled from "styled-components";

const FooterContainer = styled(Container)`
    background-color: Black;
    display: flex;
    flex-direction: column;
    align-items: center;
    position: static;
    left: 0px;
    flex: none;
    flex-grow: 0;
    margin: 0px 0px;
`;

const FooterLink = styled(Row)`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    padding: 16px 48px;
    position: static;
    flex: none;
    flex-grow: 0;
    margin: 8px 0px;
    width: 100%
`;

const FooterButton = styled(Button)`
    background-color: MediumTurquoise;
    border: none;
    position: static;
    top: 16px;
    flex: none;
    flex-grow: 0;
    margin: 0px 16px;
`;

function Footer() {
	return (
		<div style={{'background-color': 'Black', 'padding': '16px', 'align-items': 'center', 'display': 'flex'}}>
			<FooterLink>
				<Col class="col-md-auto">
				    <FooterButton>Testing</FooterButton>
				</Col>
                <Col class="col-md-auto">
                    <FooterButton>Testing</FooterButton>
                </Col>
                <Col class="col-md-auto">
                    <FooterButton>Testing</FooterButton>
                </Col>
			</FooterLink>
		</div>
	);
}

export default Footer;