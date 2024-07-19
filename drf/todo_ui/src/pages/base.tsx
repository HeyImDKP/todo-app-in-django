import React from 'react'
import { Button } from '@mui/material'
import { AppBar, Box, Toolbar, IconButton, Typography } from '@mui/material'
import { Menu as MenuIcon } from '@mui/icons-material'
import styles from './css_modules/base.module.css'

class Base_Page<P, S> extends React.Component<{} & P, {} & S> {
  colors = {
    dark: '#333',
    light: '#f5f5f5',
    yellow: '#feefcc',
    cream: '#fcde99',
    darkYellow: '#fed668',
    gray: '#696d72',
    red: '#e53f3f',
    darkRed: '#b91c1c',
  }

  navbarStyle = {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
  }

  constructor(props: any) {
    super(props)
  }

  display_navbar() {
    return (
      <>
        <AppBar component='header' position="sticky">
          <Toolbar>
            <IconButton
              size="large"
              edge="start"
              color="inherit"
              aria-label="menu"
              sx={{ mr: 2 }}
            >
              <MenuIcon />
            </IconButton>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              Todo
            </Typography>
            <Button color="inherit">Login</Button>
          </Toolbar>
        </AppBar>
      </>
    )
  }

  render() {
    return (
      <>
        {this.display_navbar()}
        <Box sx={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
        }}>

        </Box>

      </>
    )
  }
}

export default Base_Page
