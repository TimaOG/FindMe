import '../App.css'
import React from 'react';
import { Link } from '@react-navigation/native';
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import logo from '../logo.png';
import {Text} from 'react-native';

function Authorization ({navigation}){
        return (
            <Container maxWidth="sm">
                <Box
                className='BoxAuth'>
                    <Box
                    className='LogoBox'
                    >
                        <img
                        className='ImageLogo'
                        src={logo} 
                        alt="Logo" />
                        <Text
                        className='TextLogo'
                        >FindeMe</Text>
                    </Box>
                    
                    <Link
                    to={{ screen: 'Authorization'}}
                    >Go to Registration</Link>
                </Box>
                
            </Container>
        );
}

export default Authorization;