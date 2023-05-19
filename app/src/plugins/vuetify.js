import {createVuetify, } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'


const myCustomLightTheme = {
    dark: false,
    colors: {
        background: '#FFFFFF',
        surface: '#FFFFFF',
        primary: '#0792a9',
        'primary-darken-1': '#3700B3',
        secondary: '#03DAC6',
        'secondary-darken-1': '#018786',
        error: '#B00020',
        info: '#2196F3',
        success: '#4CAF50',
        warning: '#FB8C00',
    },
}

export default createVuetify({
    components,
    directives,
    theme: {
        defaultTheme: 'myCustomLightTheme',
        themes: {
            myCustomLightTheme,
        },
    },
})