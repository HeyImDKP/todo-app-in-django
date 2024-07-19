import { Box, Button, Divider, Typography } from '@mui/material'
import { CheckCircle, Cancel } from '@mui/icons-material';
import * as React from 'react'
import Base_Page from './base'
import axios, { AxiosResponse } from 'axios'
import styles from './css_modules/homepage.module.css'

interface Todo_t {
  id: number
  title: string
  details: string
  done: boolean
  date: Date
}

interface TodoList_t {
  todoData?: Todo_t[]
}

class Home_Page extends Base_Page<{}, TodoList_t> {
  todoStatus = false

  apiInstance = axios.create({
    baseURL: 'http://localhost:8081/api/',
    timeout: 1000,
    auth: {
      username: 'davekevin',
      password: 'password',
    },
  })

  constructor(props: any) {
    super(props)
    this.state = {
      todoData: []
    }
  }

  get_todo_data() {
    this.apiInstance
      .get('todo/', {
        params: {
          page_size: 10,
        },
      })
      .then((response: AxiosResponse<Todo_t[]>) => {
        this.setState({
          todoData: response.data
            .map((todo: Todo_t) => ({ ...todo, date: new Date(todo.date) }))
        })
      }).catch(() => {
        this.setState({
          todoData: []
        })
      })
  }

  set_todo_done(id: number) {
    this.apiInstance
      .patch(`todo/${id}/`, {
        done: !this.state.todoData?.find((todo: Todo_t) => todo.id === id)?.done
      })
      .then(() => {
        this.get_todo_data()
      }).catch(() => {

      })
  }

  display_todo_data() {
    if (!this.todoStatus) {
      this.get_todo_data()
      this.todoStatus = true
    }
    return this.state.todoData?.map((todo: Todo_t) => (
      <React.Fragment key={todo.id} >
        <Box className={styles.todoContainer}>
          <Box className={styles.todo}>
            <Typography>Todo: {todo.title}</Typography>
            <Typography>Date: {todo.date.toLocaleString()}</Typography>
            <Typography>Details: {todo.details}</Typography>
          </Box>
          <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
            <Divider
              sx={{ borderRight: '2px solid var(--dark)', borderRadius: '20px' }}
              orientation="vertical"
              variant='middle'
              flexItem
            />
          </Box>
          <Box className={styles.doneContainer}>
            <Button
              className={styles.doneButton}
              onClick={() => this.set_todo_done(todo.id)}
              endIcon={todo.done ? <CheckCircle htmlColor='var(--dark)' /> : <Cancel htmlColor='var(--dark)' />}
            >
              <Typography
                sx={{ color: 'var(--dark)', textTransform: 'capitalize' }}
                variant='body1'
              >
                {todo.done ? 'Done' : 'Not Done'}
              </Typography>
            </Button>
          </Box>
        </Box>
      </React.Fragment>
    ))
  }

  display_todo_title() {
    return (
      <Box className={styles.title}>
        <Typography variant='h1'>
          Todo List
        </Typography>
      </Box>
    )
  }

  render() {
    return (
      <>
        {this.display_navbar()}
        <Box sx={{ flex: 1, }}>
          {this.display_todo_title()}
          {this.display_todo_data()}
        </Box>
      </>
    )
  }
}

export default Home_Page