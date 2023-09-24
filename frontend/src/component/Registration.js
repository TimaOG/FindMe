import '../App.css'
import React, { useState } from 'react';
import { Link } from '@react-navigation/native';
import Row from 'react-bootstrap/Row';
import Box from '@mui/material/Box';
import logo from '../logo.png';
import Wrapper from '../wrapper.png';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import axios from 'axios'
import $ from 'jquery'

function Registration({ navigation }) {
    const [formData, setFormData] = useState({
        fio: '',
        login: '',
        password: '',
        password2: '',
        email: '',
        sex: true,
        birthdate: '2023-04-23'
    });
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };
    const handleSubmit = (event) => {
        event.preventDefault();
            // axios.post('http://localhost:8000/register', formData).then(response =>{
            //     console.log(response.data);
            // })
            // .catch(error =>{
            //     console.log(error);
            // });
            console.log(formData)
            $.ajax({
                url: 'http://localhost:8000/register',
                type: 'POST',
                data: JSON.stringify({
                    fio: 'gang',
                    login: 'gang',
                    password: '123',
                    password2: '123',
                    email: 'gg@gg.ru',
                    sex: true,
                    birthdate: '2023-09-01'
                }),
                contentType: 'application/json; charset=utf-8',
                dataType: 'json',
                success: function (data) {
                    console.log(data);
                },
                error: function (error) {
                    console.log(error);
                }
            });
        };
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
                            to={{ screen: 'Authorization' }}
                        >
                            <p className='pNamesReg'>Do you want to<p className='pNamesRegColor'>authorization?</p></p>
                        </Link>
                    </Row>
                    <Row>
                        <Form id='myForm' onSubmit={handleSubmit}>
                            <Form.Group className='FormGroupInp' controlId="exampleForm.ControlInput1">
                                <Row className='RowInputs'>
                                    <Form.Label className='EmailText'>Email</Form.Label>
                                    <Form.Control className='formRow' type="email" name='email' placeholder="Email" value={formData.email} onChange={handleInputChange} />
                                </Row>
                            </Form.Group>
                            <Form.Group className='FormGroupInp' controlId="formBasicPassword">
                                <Row className='RowInputs'>
                                    <Form.Label className='PassText'>Name</Form.Label>
                                    <Form.Control className='formRow' type="name" name='fio' placeholder="Name" value={formData.fio} onChange={handleInputChange} />
                                </Row>
                            </Form.Group>
                            <Form.Group className='FormGroupInp' controlId="formBasicPassword">
                                <Row className='RowInputs'>
                                    <Form.Label className='PassText'>Login</Form.Label>
                                    <Form.Control className='formRow' type="name" name='login' placeholder="Login" value={formData.login} onChange={handleInputChange} />
                                </Row>
                            </Form.Group>
                            <Form.Group className='FormGroupInp' controlId="formBasicPassword">
                                <Row className='RowInputs'>
                                    <Form.Label className='PassText'>Password</Form.Label>
                                    <Form.Control className='formRow' type="password" name='password' placeholder="Password" value={formData.password} onChange={handleInputChange} />
                                </Row>
                            </Form.Group>
                            <Form.Group className='FormGroupInp' controlId="formBasicPassword">
                                <Row className='RowInputs'>
                                    <Form.Label className='PassText'>Repeat password</Form.Label>
                                    <Form.Control className='formRow' type="password" name='password2' placeholder="Password" value={formData.password2} onChange={handleInputChange} />
                                </Row>
                            </Form.Group>
                            <Row>
                                <Button className='SubmitForm' type="submit">
                                    Registration
                                </Button>
                            </Row>
                        </Form>
                    </Row>
                </Box>
            </Container>
        );
    }

    export default Registration;

