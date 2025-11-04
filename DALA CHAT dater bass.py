import React, { useState } from 'react';
import {
  Send,
  User,
  MessageCircle,
  Users,
  Database,
  Wifi,
  CheckCircle,
  XCircle,
  Eye,
  Code,
} from 'lucide-react';

/* -------------------------------------------------
   COMPONENT ENTRY POINT
   ------------------------------------------------- */
export default function BackendDemo() {
  /* ------------------- STATE ------------------- */
  // Current active tab (overview | api | websocket | database)
  const [activeTab, setActiveTab] = useState('overview');
  // Recent API test results (max 10)
  const [testResults, setTestResults] = useState([]);
  // WebSocket connection toggle
  const [isConnected, setIsConnected] = useState(false);

  /* ------------------- DATA ------------------- */
  // REST API endpoint definitions
  const apiEndpoints = [
    /* REGISTER USER */
    {
      method: 'POST',
      path: '/api/auth/register',
      description: 'Register a new user',
      body: {
        username: 'john',
        email: 'john@example.com',
        password: 'password123',
        name: 'John Doe',
      },
      response: {
        token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...',
        user: {
          id: 1,
          username: 'john',
          email: 'john@example.com',
          name: 'John Doe',
          avatar: 'User',
        },
      },
    },
    /* LOGIN USER */
    {
      method: 'POST',
      path: '/api/auth/login',
      description: 'Login user and get token',
      body: {
        email: 'john@example.com',
        password: 'password123',
      },
      response: {
        token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...',
        user: {
          id: 1,
          username: 'john',
          name: 'John Doe',
          avatar: 'Man',
        },
      },
    },
    /* GET ALL USERS (CONTACTS) */
    {
      method: 'GET',
      path: '/api/users',
      description: 'Get all users (contacts)',
      headers: { Authorization: 'Bearer {token}' },
      response: [
        { id: 2, username: 'jane', name: 'Jane Smith', avatar: 'Woman', status: 'online' },
        { id: 3, username: 'mike', name: 'Mike Johnson', avatar: 'Man in suit', status: 'offline' },
      ],
    },
    /* GET CONVERSATION WITH USER */
    {
      method: 'GET',
      path: '/api/messages/:userId',
      description: 'Get conversation with specific user',
      headers: { Authorization: 'Bearer {token}' },
      response: [
        {
          id: 1,
          senderId: 1,
          receiverId: 2,
          text: 'Hello!',
          timestamp: '2024-01-15T10:30:00',
          status: 'read',
        },
        {
          id: 2,
          senderId: 2,
          receiverId: 1,
          text: 'Hi there!',
          timestamp: '2024-01-15T10:31:00',
          status: 'read',
        },
      ],
    },
    /* SEND NEW MESSAGE */
    {
      method: 'POST',
      path: '/api/messages',
      description: 'Send a new message',
      headers: { Authorization: 'Bearer {token}' },
      body: {
        receiverId: 2,
        text: 'Hello, how are you?',
      },
      response: {
        id: 3,
        senderId: 1,
        receiverId: 2,
        text: 'Hello, how are you?',
        timestamp: '2024-01-15T10:35:00',
        status: 'sent',
      },
    },
    /* GET ALL CONVERSATIONS */
    {
      method: 'GET',
      path: '/api/conversations',
      description: 'Get all conversations',
      headers: { Authorization: 'Bearer {token}' },
      response: [
        {
          user: { id: 2, name: 'Jane Smith', avatar: 'Woman', status: 'online' },
          lastMessage: { text: 'See you later!', timestamp: '2024-01-15T10:40:00' },
          unreadCount: 0,
        },
      ],
    },
  ];

  // WebSocket event definitions
  const socketEvents = [
    /* REGISTER CONNECTION */
    {
      event: 'register',
      direction: 'emit',
      description: 'Register user connection',
      data: { userId: 1 },
      color: 'bg-blue-100 text-blue-800',
    },
    /* SEND MESSAGE */
    {
      event: 'send_message',
      direction: 'emit',
      description: 'Send message to another user',
      data: { senderId: 1, receiverId: 2, text: 'Hello!' },
      color: 'bg-green-100 text-green-800',
    },
    /* RECEIVE NEW MESSAGE */
    {
      event: 'new_message',
      direction: 'listen',
      description: 'Receive new message',
      data: { id: 1, senderId: 2, text: 'Hi!', timestamp: '2024-01-15T10:30:00' },
      color: 'bg-purple-100 text-purple-800',
    },
    /* USER STATUS CHANGE */
    {
      event: 'user_status_change',
      direction: 'listen',
      description: 'User goes online/offline',
      data: { userId: 2, status: 'online' },
      color: 'bg-yellow-100 text-yellow-800',
    },
    /* TYPING INDICATOR */
    {
      event: 'typing',
      direction: 'emit',
      description: 'User is typing',
      data: { senderId: 1, receiverId: 2 },
      color: 'bg-indigo-100 text-indigo-800',
    },
    /* MESSAGE DELIVERED */
    {
      event: 'message_delivered',
      direction: 'listen',
      description: 'Message delivered confirmation',
      data: { messageId: 1 },
      color: 'bg-teal-100 text-teal-800',
    },
    /* MARK MESSAGE READ */
    {
      event: 'message_read',
      direction: 'emit',
      description: 'Mark message as read',
      data: { messageId: 1, senderId: 2 },
      color: 'bg-pink-100 text-pink-800',
    },
  ];

  // Database schema definition
  const databaseSchema = {
    users: {
      fields: [
        'id',
        'username',
        'email',
        'password',
        'name',
        'avatar',
        'status',
        'lastSeen',
        'createdAt',
      ],
      example: {
        id: 1,
        username: 'john',
        email: 'john@example.com',
        password: '$2a$10$hash...',
        name: 'John Doe',
        avatar: 'Man',
        status: 'online',
        lastSeen: null,
        createdAt: '2024-01-15T09:00:00',
      },
    },
    messages: {
      fields: ['id', 'senderId', 'receiverId', 'text', 'timestamp', 'status'],
      example: {
        id: 1,
        senderId: 1,
        receiverId: 2,
        text: 'Hello!',
        timestamp: '2024-01-15T10:30:00',
        status: 'read',
      },
    },
  };

  /* ------------------- HELPERS ------------------- */
  // Simulate an API call and store the result
  const simulateTest = (endpoint) => {
    const result = {
      endpoint: `${endpoint.method} ${endpoint.path}`,
      status: 200,
      time: Math.random() * 100 + 50,
      timestamp: new Date().toLocaleTimeString(),
    };
    setTestResults((prev) => [result, ...prev.slice(0, 9)]);
  };

  /* -------------------------------------------------
     RENDER
     ------------------------------------------------- */
  return (
    /* PAGE CONTAINER */
    <div className="min-h-screen bg-gradient-to-br from-green-50 to-blue-50 p-6">
      <div className="max-w-7xl mx-auto">
        {/* ---------- HEADER ---------- */}
        <div className="bg-white rounded-2xl shadow-xl p-8 mb-6">
          <div className="flex items-center justify-between">
            <div>
              {/* Title – re-branded */}
              <h1 className="text-4xl font-bold text-gray-900 mb-2">
                DALA Backend API IOP
              </h1>
              <p className="text-gray-600">
                Complete backend server with real-time messaging
              </p>
            </div>

            {/* Connection status + toggle */}
            <div className="flex items-center gap-4">
              <div
                className={`flex items-center gap-2 px-4 py-2 rounded-full ${
                  isConnected ? 'bg-green-100' : 'bg-gray-100'
                }`}
              >
                <Wifi
                  className={`w-5 h-5 ${
                    isConnected ? 'text-green-600' : 'text-gray-400'
                  }`}
                />
                <span
                  className={`font-semibold ${
                    isConnected ? 'text-green-700' : 'text-gray-500'
                  }`}
                >
                  {isConnected ? 'Connected' : 'Disconnected'}
                </span>
              </div>
              <button
                onClick={() => setIsConnected(!isConnected)}
                className="bg-green-500 hover:bg-green-600 text-white px-6 py-2 rounded-full font-semibold transition-colors"
              >
                {isConnected ? 'Disconnect' : 'Connect'}
              </button>
            </div>
          </div>
        </div>

        {/* ---------- TABS ---------- */}
        <div className="flex gap-2 mb-6">
          {[
            { id: 'overview', label: 'Overview', icon: Eye },
            { id: 'api', label: 'API Endpoints', icon: Code },
            { id: 'websocket', label: 'WebSocket', icon: Wifi },
            { id: 'database', label: 'Database', icon: Database },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`flex items-center gap-2 px-6 py-3 rounded-xl font-semibold transition-all ${
                activeTab === tab.id
                  ? 'bg-white shadow-lg text-green-600'
                  : 'bg-white/50 text-gray-600 hover:bg-white'
              }`}
            >
              <tab.icon className="w-5 h-5" />
              {tab.label}
            </button>
          ))}
        </div>

        {/* ---------- MAIN GRID ---------- */}
        <div className="grid grid-cols-3 gap-6">
          {/* LEFT COLUMN – CONTENT */}
          <div className="col-span-2">
            {/* OVERVIEW TAB */}
            {activeTab === 'overview' && (
              <div className="space-y-6">
                {/* FEATURES */}
                <div className="bg-white rounded-2xl shadow-lg p-8">
                  <h2 className="text-2xl font-bold text-gray-900 mb-6">
                    Backend Features
                  </h2>
                  <div className="grid grid-cols-2 gap-4">
                    {[
                      {
                        icon: User,
                        label: 'User Authentication',
                        desc: 'JWT-based auth with bcrypt',
                      },
                      {
                        icon: MessageCircle,
                        label: 'Real-time Messaging',
                        desc: 'Socket.IO powered chat',
                      },
                      {
                        icon: Users,
                        label: 'Contact Management',
                        desc: 'User list and profiles',
                      },
                      {
                        icon: Database,
                        label: 'Message Storage',
                        desc: 'Persistent message history',
                      },
                      {
                        icon: CheckCircle,
                        label: 'Message Status',
                        desc: 'Sent, delivered, read',
                      },
                      {
                        icon: Wifi,
                        label: 'Online Status',
                        desc: 'Live presence tracking',
                      },
                    ].map((feature, idx) => (
                      <div
                        key={idx}
                        className="flex items-start gap-4 p-4 bg-gray-50 rounded-xl"
                      >
                        <div className="bg-green-100 p-3 rounded-lg">
                          <feature.icon className="w-6 h-6 text-green-600" />
                        </div>
                        <div>
                          <h3 className="font-semibold text-gray-900">
                            {feature.label}
                          </h3>
                          <p className="text-sm text-gray-600">
                            {feature.desc}
                          </p>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                {/* TECH STACK */}
                <div className="bg-white rounded-2xl shadow-lg p-8">
                  <h2 className="text-2xl font-bold text-gray-900 mb-4">
                    Tech Stack
                  </h2>
                  <div className="grid grid-cols-3 gap-4">
                    {[
                      { name: 'Node.js', desc: 'Runtime environment' },
                      { name: 'Express', desc: 'Web framework' },
                      { name: 'Socket.IO', desc: 'Real-time engine' },
                      { name: 'JWT', desc: 'Authentication' },
                      { name: 'Bcrypt', desc: 'Password hashing' },
                      { name: 'CORS', desc: 'Cross-origin requests' },
                    ].map((tech, idx) => (
                      <div
                        key={idx}
                        className="p-4 bg-gradient-to-br from-green-50 to-blue-50 rounded-xl"
                      >
                        <h3 className="font-bold text-gray-900">
                          {tech.name}
                        </h3>
                        <p className="text-sm text-gray-600">{tech.desc}</p>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            )}

            {/* API ENDPOINTS TAB */}
            {activeTab === 'api' && (
              <div className="bg-white rounded-2xl shadow-lg p-8">
                <h2 className="text-2xl font-bold text-gray-900 mb-6">
                  REST API Endpoints
                </h2>
                <div className="space-y-4">
                  {apiEndpoints.map((endpoint, idx) => (
                    <div
                      key={idx}
                      className="border border-gray-200 rounded-xl overflow-hidden"
                    >
                      {/* Endpoint header */}
                      <div className="bg-gray-50 p-4 flex items-center justify-between">
                        <div className="flex items-center gap-4">
                          <span
                            className={`px-3 py-1 rounded-lg text-sm font-bold ${
                              endpoint.method === 'GET'
                                ? 'bg-blue-100 text-blue-700'
                                : endpoint.method === 'POST'
                                ? 'bg-green-100 text-green-700'
                                : 'bg-purple-100 text-purple-700'
                            }`}
                          >
                            {endpoint.method}
                          </span>
                          <code className="text-sm font-mono text-gray-900">
                            {endpoint.path}
                          </code>
                        </div>
                        <button
                          onClick={() => simulateTest(endpoint)}
                          className="text-green-600 hover:text-green-700 font-semibold text-sm"
                        >
                          Test →
                        </button>
                      </div>

                      {/* Endpoint details */}
                      <div className="p-4">
                        <p className="text-gray-600 mb-3">
                          {endpoint.description}
                        </p>

                        {/* Request body (if any) */}
                        {endpoint.body && (
                          <div className="mb-3">
                            <p className="text-xs font-semibold text-gray-500 mb-1">
                              REQUEST BODY:
                            </p>
                            <pre className="bg-gray-900 text-green-400 p-3 rounded-lg text-xs overflow-x-auto">
                              {JSON.stringify(endpoint.body, null, 2)}
                            </pre>
                          </div>
                        )}

                        {/* Response */}
                        <div>
                          <p className="text-xs font-semibold text-gray-500 mb-1">
                            RESPONSE:
                          </p>
                          <pre className="bg-gray-900 text-blue-400 p-3 rounded-lg text-xs overflow-x-auto">
                            {JSON.stringify(endpoint.response, null, 2)}
                          </pre>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* WEBSOCKET EVENTS TAB */}
            {activeTab === 'websocket' && (
              <div className="bg-white rounded-2xl shadow-lg p-8">
                <h2 className="text-2xl font-bold text-gray-900 mb-6">
                  WebSocket Events
                </h2>
                <div className="space-y-3">
                  {socketEvents.map((event, idx) => (
                    <div
                      key={idx}
                      className="border border-gray-200 rounded-xl p-4"
                    >
                      {/* Event header */}
                      <div className="flex items-center justify-between mb-3">
                        <div className="flex items-center gap-3">
                          <span
                            className={`px-3 py-1 rounded-lg text-xs font-bold ${event.color}`}
                          >
                            {event.direction === 'emit' ? 'EMIT' : 'LISTEN'}
                          </span>
                          <code className="text-sm font-mono font-semibold text-gray-900">
                            {event.event}
                          </code>
                        </div>
                      </div>

                      <p className="text-sm text-gray-600 mb-2">
                        {event.description}
                      </p>

                      {/* Payload */}
                      <pre className="bg-gray-900 text-yellow-400 p-3 rounded-lg text-xs overflow-x-auto">
                        {JSON.stringify(event.data, null, 2)}
                      </pre>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* DATABASE SCHEMA TAB */}
            {activeTab === 'database' && (
              <div className="bg-white rounded-2xl shadow-lg p-8">
                <h2 className="text-2xl font-bold text-gray-900 mb-6">
                  Database Schema
                </h2>
                <div className="space-y-6">
                  {Object.entries(databaseSchema).map(([table, data]) => (
                    <div
                      key={table}
                      className="border border-gray-200 rounded-xl overflow-hidden"
                    >
                      {/* Table header */}
                      <div className="bg-gradient-to-r from-green-500 to-blue-500 p-4">
                        <h3 className="text-xl font-bold text-white">
                          Table {table}
                        </h3>
                      </div>

                      <div className="p-4">
                        {/* Fields */}
                        <div className="mb-4">
                          <p className="text-sm font-semibold text-gray-500 mb-2">
                            FIELDS:
                          </p>
                          <div className="flex flex-wrap gap-2">
                            {data.fields.map((field, idx) => (
                              <span
                                key={idx}
                                className="px-3 py-1 bg-gray-100 rounded-full text-sm font-mono text-gray-700"
                              >
                                {field}
                              </span>
                            ))}
                          </div>
                        </div>

                        {/* Example row */}
                        <div>
                          <p className="text-sm font-semibold text-gray-500 mb-2">
                            EXAMPLE:
                          </p>
                          <pre className="bg-gray-900 text-green-400 p-4 rounded-lg text-xs overflow-x-auto">
                            {JSON.stringify(data.example, null, 2)}
                          </pre>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* RIGHT COLUMN – SIDEBAR */}
          <div className="space-y-6">
            {/* SERVER STATUS */}
            <div className="bg-white rounded-2xl shadow-lg p-6">
              <h3 className="font-bold text-gray-900 mb-4 flex items-center gap-2">
                <CheckCircle className="w-5 h-5 text-green-600" />
                Server Status
              </h3>
              <div className="space-y-3">
                <div className="flex justify-between items-center">
                  <span className="text-gray-600">Port</span>
                  <span className="font-mono font-semibold text-gray-900">
                    5000
                  </span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-600">Users</span>
                  <span className="font-semibold text-gray-900">2</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-600">Messages</span>
                  <span className="font-semibold text-gray-900">0</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-600">Connected</span>
                  <span className="font-semibold text-gray-900">
                    {isConnected ? '1' : '0'}
                  </span>
                </div>
              </div>
            </div>

            {/* TEST USERS */}
            <div className="bg-white rounded-2xl shadow-lg p-6">
              <h3 className="font-bold text-gray-900 mb-4">Test Users</h3>
              <div className="space-y-3">
                {[
                  { name: 'John Doe', email: 'john@example.com', avatar: 'Man' },
                  { name: 'Jane Smith', email: 'jane@example.com', avatar: 'Woman' },
                ].map((user, idx) => (
                  <div
                    key={idx}
                    className="flex items-center gap-3 p-3 bg-gray-50 rounded-xl"
                  >
                    <div className="text-2xl">{user.avatar}</div>
                    <div>
                      <p className="font-semibold text-gray-900 text-sm">
                        {user.name}
                      </p>
                      <p className="text-xs text-gray-500">{user.email}</p>
                    </div>
                  </div>
                ))}
                <div className="pt-2 border-t border-gray-200">
                  <p className="text-xs text-gray-500">
                    Password:{' '}
                    <code className="bg-gray-100 px-2 py-1 rounded">
                      password123
                    </code>
                  </p>
                </div>
              </div>
            </div>

            {/* RECENT TESTS */}
            {testResults.length > 0 && (
              <div className="bg-white rounded-2xl shadow-lg p-6">
                <h3 className="font-bold text-gray-900 mb-4">
                  Recent Tests
                </h3>
                <div className="space-y-2">
                  {testResults.map((result, idx) => (
                    <div
                      key={idx}
                      className="flex items-center gap-2 text-xs"
                    >
                      <CheckCircle className="w-4 h-4 text-green-600" />
                      <span className="text-gray-500">{result.timestamp}</span>
                      <span className="font-mono text-gray-900">
                        {result.status}
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
