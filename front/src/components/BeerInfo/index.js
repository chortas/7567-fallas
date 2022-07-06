import React, {useState} from 'react';
import {Card, Grid, Button, Typography, Stack} from '@mui/material';
import useStyles from './styles';

export default function BeerInfo({info}) {

    if (info?.beers?.length === 0) {
        return (
            <Card
                  sx={{
                      marginLeft: 10,
                      marginRight: 10,
                      padding: '20px 0 20px 30px',
                      background: 'transparent',
                      border: '3px solid #D3A10D',
                      borderRadius: 3,
                      width: 430,
                      fontFamily: '"Copse", serif',
                      fontWeight: '400',
                      fontSize: '15px',
                      lineHeight: '20px'
                  }}
                  elevation={0}>
                <p style={{
                    fontFamily: '"Copse", serif',
                    fontWeight: '400',
                    fontSize: '17px',
                    lineHeight: '14px'
                }}>No se encontraron cervezas con esas características</p>
            </Card>
        )
    }

    return (
        info.beers.map((beer) => (
            <Card
                sx={{
                    marginLeft: 10,
                    marginRight: 10,
                    padding: '20px 0 30px 30px',
                    background: 'transparent',
                    border: '3px solid #D3A10D',
                    borderRadius: 3,
                    width: 430,
                    fontFamily: '"Copse", serif',
                    fontWeight: '400',
                    fontSize: '15px',
                    lineHeight: '20px'
                }}
                elevation={0}>
                <Stack direction="row">
                    <div style={{margin: '-23px 0 0 -33px'}}>
                        <img
                            src={beer.foto}
                            alt="beer"
                            style={{
                                width: 164,
                                height: 230,
                                border: '3px solid #D3A10D',
                                borderRadius: '15px 0px 0px 0px',
                                objectFit: 'fill'
                            }}/>
                    </div>

                    <Stack sx={{paddingLeft: '20px', paddingRight: '20px'}}>
                        <div style={{marginBottom: '7px'}}><b>Nombre: </b>{beer.nombre}</div>
                        <div style={{marginBottom: '7px'}}><b>Color: </b>{beer.color}</div>
                        <div style={{marginTop: '15px', marginBottom: '10px', fontSize: '20px'}}><b>Ingredientes</b>
                        </div>
                        <div style={{marginBottom: '7px'}}><b>Malta: </b>{beer.maltas.join(', ')}</div>
                        <div style={{marginBottom: '7px'}}><b>Lúpulo: </b>{beer.lupulo.join(', ')}</div>
                        <div style={{marginBottom: '7px'}}><b>Levadura: </b>{beer.levadura.join(', ')}</div>
                    </Stack>
                </Stack>
                <Stack sx={{paddingRight: '30px'}}>
                    <div style={{marginTop: '15px', marginBottom: '10px', fontSize: '20px'}}><b>Preparación</b></div>
                    <div style={{marginBottom: '7px'}}><b>Maceración: </b>{beer.maceracion}</div>
                    <div style={{marginBottom: '7px'}}><b>Ebullición: </b>{beer.ebullicion}</div>
                    <div style={{marginBottom: '7px'}}><b>Fermentación: </b>{beer.fermentacion}</div>
                    <div style={{marginBottom: '7px'}}><b>Acondicionamiento: </b>{beer.acondicionamiento}</div>
                </Stack>
            </Card>
        )))
}
