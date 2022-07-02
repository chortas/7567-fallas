import React, { useState } from 'react';
import { Card, Grid, Button, Typography } from '@mui/material';
import useStyles from './styles';

export default function BeerInfo({info}) {

    if (info?.beers?.length === 0) {
        return (
            <Card sx={{ marginLeft: 10, marginRight: 10, marginTop: 5, marginBottom: 5, padding: 5 }}>
                <p>No se encontraron cervezas con esas caracteristicas :(</p>  
            </Card>
        )
    }

    return (
            info.beers.map((beer) => (
                <Card sx={{ marginLeft: 10, marginRight: 10, marginTop: 5, marginBottom: 5, padding: 5 }}>
                    <div style={{display: "flex", flexDirection: "row"}}>
                        <div style={{marginRight: 5}}>
                        <img src={beer.foto} alt="beer" style={{ width: 100 }} />
                        </div>
                    
                    <Grid container>
                        <Grid item xs={12}>
                            <p><b>Nombre: </b>{beer.nombre}</p>
                        </Grid>

                        <Grid item xs={12}>
                            <p><b>Color: </b>{beer.color}</p>
                        </Grid>


                        <Grid item xs={12}>
                            <h3>Ingredientes</h3>
                        </Grid>

                        <Grid item xs={12}>
                            <p><b>Malta: </b>{beer.maltas.join(', ')}</p>
                        </Grid>

                        <Grid item xs={12}>
                            <p><b>Lúpulo: </b>{beer.lupulo.join(', ')}</p>
                        </Grid>

                        <Grid item xs={12}>
                            <p><b>Levadura: </b>{beer.levadura.join(', ')}</p>
                        </Grid>

                        <Grid item xs={12}>
                            <h3>Preparación</h3>
                        </Grid>

                        <Grid item xs={12}>
                            <p><b>Maceración: </b>{beer.maceracion}</p>
                        </Grid>

                        <Grid item xs={12}>
                            <p><b>Ebullición: </b>{beer.ebullicion}</p>
                        </Grid>

                        <Grid item xs={12}>
                            <p><b>Fermentación: </b>{beer.fermentacion}</p>
                        </Grid>

                        <Grid item xs={12}>
                            <p><b>Acondicionamiento: </b>{beer.acondicionamiento}</p>
                        </Grid>
                    </Grid>
                    </div>
                    
                </Card>
    )))
    }