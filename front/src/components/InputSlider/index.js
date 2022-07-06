import React from 'react';
import {Grid, Slider, Tooltip} from '@mui/material';
import HelpIcon from '@mui/icons-material/Help';
import useStyles from './styles';

export default function InputSlider({
                                        max,
                                        title,
                                        tooltip,
                                        value,
                                        handleValueChange,
                                        step = 1,
                                        titleSize = 6,
                                        sliderSize = 6
                                    }) {
    const classes = useStyles();

    const marks = [
        {
            value: 0,
            label: '0',
        },
        {
            value: max,
            label: `${max}`,
        },
    ];

    return (
        <>
            <Grid className={classes.firstSliderGrid} item xs={titleSize} style={{paddingTop: '18px'}}>
                <Grid container className={classes.titles}>
                    <div style={{marginTop: '3px'}}>
                        {title}
                    </div>
                    <Tooltip className={classes.tooltips} placement="right"
                             title={<span className={classes.tooltipsText}>{tooltip}</span>}>
                        <HelpIcon color="action" fontSize="small"></HelpIcon>
                    </Tooltip>
                </Grid>
            </Grid>
            <Grid className={classes.firstSliderGrid} item xs={sliderSize} style={{paddingTop: '18px'}}>
                <Slider
                    size="small"
                    value={value}
                    aria-labelledby="discrete-slider-always"
                    step={step}
                    max={max}
                    marks={marks}
                    onChange={handleValueChange}
                    valueLabelDisplay="on"
                    defaultValue={10}
                    sx={{
                        color: '#D3A10D',
                        width: '170px',
                    }}
                />
            </Grid>
        </>
    );
}
