import '../App.css'
import React from 'react';
import { Link } from '@react-navigation/native';
import Row from 'react-bootstrap/Row';
import Box from '@mui/material/Box';
import logo from '../logo.png';
import Wrapper from '../wrapper.png';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

function Authorization ({navigation}){
        return (
            <Container fluid="md" className='ContainerAuth'>
                <Box
                className='BoxAuth'>
                    <Row>
                        <Box
                        className='LogoBox'
                        >
                            <img
                            className='ImageLogo'
                            src={logo} 
                            alt="Logo" />
                            <h1
                            className='TextLogo'
                            >FindeMe</h1>
                        </Box>
                        <img
                            className='ImageWrapper'
                            src={Wrapper} 
                            alt="ImageWrapper" />
                    </Row>
                    <Row>
                        <Link
                            to={{ screen: 'Registration'}}
                            >
                            <p className='pNamesReg'>Do you want to<p className='pNamesRegColor'>register?</p></p>
                        </Link>
                    </Row>
                    <Row>
                        <Form>
                            <Form.Group className='FormGroupInp' controlId="exampleForm.ControlInput1">
                                <Row className='RowInputs'>
                                    <Form.Label className='EmailText'>Email</Form.Label>
                                    <Form.Control className='formRow' type="email" placeholder="Email" />
                                </Row> 
                            </Form.Group>
                            <Form.Group className='FormGroupInp' controlId="formBasicPassword">
                                <Row className='RowInputs'>
                                    <Form.Label className='PassText'>Password</Form.Label>
                                    <Form.Control className='formRow' type="password" placeholder="Password" />
                                </Row>  
                            </Form.Group>
                            <Row>
                                <Button className='SubmitForm' type="submit">
                                    Sign In
                                </Button>
                            </Row>
                            
                        </Form>
                    </Row>
                </Box>
                
            </Container>
        );
}

export default Authorization;