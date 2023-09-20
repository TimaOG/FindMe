import * as React from 'react';
import { Button, View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

function Registration ({navigation}){
        return (
            <Button
                title="Go to Authorization"
                onPress={() => navigation.navigate('Authorization')}
            />
        );
}

export default Registration;

