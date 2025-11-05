import React, { useState, useEffect, useRef } from 'react';
import { Send, Search, Menu, UserPlus, MessageCircle, Image, Paperclip, Smile, MoreVertical, Phone, Video, User } from 'lucide-react';

export default function DalaChatApp() {
  const [currentView, setCurrentView] = useState('login');
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [currentUser, setCurrentUser] = useState(null);
  const [conversations, setConversations] = useState([]);
  const [selectedChat, setSelectedChat] = useState(null);
  const [messages, setMessages] = useState([]);
  const [messageInput, setMessageInput] = useState('');
  const [searchQuery, setSearchQuery] = useState('');
  const [showSidebar, setShowSidebar] = useState(true);
  
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [username, setUsername] = useState('');
  const [fullName, setFullName] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    if (isLoggedIn) {
      setConversations([
        {
          id: 1,
          name: 'John Doe',
          lastMessage: 'Hey! How are you doing?',
          time: '10:30 AM',
          unread: 2,
          avatar: '👨‍💼',
          online: true
        },
        {
          id: 2,
          name: 'Team Project',
          lastMessage: 'Meeting at 3 PM',
          time: 'Yesterday',
          unread: 0,
          avatar: '👥',
          online: false,
          isGroup: true
        },
        {
          id: 3,
          name: 'Sarah Wilson',
          lastMessage: 'Thanks for the help!',
          time: '2 days ago',
          unread: 0,
          avatar: '👩‍💼',
          online: true
        }
      ]);
    }
  }, [isLoggedIn]);

  useEffect(() => {
    if (selectedChat) {
      setMessages([
        {
          id: 1,
          sender: 'John Doe',
          text: 'Hey! How are you doing?',
          time: '10:30 AM',
          isMine: false
        },
        {
          id: 2,
          sender: 'You',
          text: 'I\'m doing great! Thanks for asking.',
          time: '10:31 AM',
          isMine: true
        },
        {
          id: 3,
          sender: 'John Doe',
          text: 'That\'s awesome! Want to grab coffee later?',
          time: '10:32 AM',
          isMine: false
        },
        {
          id: 4,
          sender: 'You',
          text: 'Sure! What time works for you?',
          time: '10:33 AM',
          isMine: true
        }
      ]);
    }
  }, [selectedChat]);

  const handleLogin = (e) => {
    e.preventDefault();
    setError('');
    
    if (!email || !password) {
      setError('Please fill in all fields');
      return;
    }

    setCurrentUser({ email, username: email.split('@')[0] });
    setIsLoggedIn(true);
    setCurrentView('chat');
    setSuccess('Login successful!');
  };

  const handleSignup = (e) => {
    e.preventDefault();
    setError('');
    
    if (!email || !password || !username) {
      setError('Email, password, and username are required');
      return;
    }

    setSuccess('Account created! Check your email to verify your account.');
    setTimeout(() => {
      setCurrentView('login');
      setSuccess('');
    }, 3000);
  };

  const handleSendMessage = () => {
    if (messageInput.trim()) {
      const newMessage = {
        id: messages.length + 1,
        sender: 'You',
        text: messageInput,
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        isMine: true
      };
      setMessages([...messages, newMessage]);
      setMessageInput('');
    }
  };

  if (currentView === 'login') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-600 via-purple-600 to-pink-500 flex items-center justify-center p-4">
        <div className="bg-white rounded-2xl shadow-2xl w-full max-w-md p-8">
          <div className="text-center mb-8">
            <div className="text-5xl mb-4">💬</div>
            <h1 className="text-3xl font-bold text-gray-800 mb-2">DALA Chat</h1>
            <p className="text-gray-600">Sign in to continue</p>
          </div>

          {error && (
            <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
              {error}
            </div>
          )}

          {success && (
            <div className="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded mb-4">
              {success}
            </div>
          )}

          <div className="space-y-4">
            <div>
              <label className="block text-gray-700 text-sm font-semibold mb-2">Email</label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="your@email.com"
              />
            </div>

            <div>
              <label className="block text-gray-700 text-sm font-semibold mb-2">Password</label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="••••••••"
              />
            </div>

            <button
              onClick={handleLogin}
              className="w-full bg-gradient-to-r from-blue-600 to-purple-600 text-white font-semibold py-3 rounded-lg hover:shadow-lg transition-all"
            >
              Sign In
            </button>
          </div>

          <div className="mt-6 text-center">
            <p className="text-gray-600">
              Don't have an account?{' '}
              <button
                onClick={() => setCurrentView('signup')}
                className="text-blue-600 font-semibold hover:underline"
              >
                Sign Up
              </button>
            </p>
          </div>
        </div>
      </div>
    );
  }

  if (currentView === 'signup') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-600 via-purple-600 to-pink-500 flex items-center justify-center p-4">
        <div className="bg-white rounded-2xl shadow-2xl w-full max-w-md p-8 max-h-screen overflow-y-auto">
          <div className="text-center mb-8">
            <div className="text-5xl mb-4">🚀</div>
            <h1 className="text-3xl font-bold text-gray-800 mb-2">Create Account</h1>
            <p className="text-gray-600">Join DALA Chat today</p>
          </div>

          {error && (
            <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4 text-sm">
              {error}
            </div>
          )}

          {success && (
            <div className="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded mb-4 text-sm">
              {success}
            </div>
          )}

          <div className="space-y-4">
            <div>
              <label className="block text-gray-700 text-sm font-semibold mb-2">Email *</label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="your@email.com"
              />
            </div>

            <div>
              <label className="block text-gray-700 text-sm font-semibold mb-2">Username *</label>
              <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="johndoe"
              />
            </div>

            <div>
              <label className="block text-gray-700 text-sm font-semibold mb-2">Password *</label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="••••••••"
              />
            </div>

            <div>
              <label className="block text-gray-700 text-sm font-semibold mb-2">Full Name</label>
              <input
                type="text"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="John Doe"
              />
            </div>

            <div>
              <label className="block text-gray-700 text-sm font-semibold mb-2">Phone Number</label>
              <input
                type="tel"
                value={phoneNumber}
                onChange={(e) => setPhoneNumber(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="+1 234 567 8900"
              />
            </div>

            <button
              onClick={handleSignup}
              className="w-full bg-gradient-to-r from-blue-600 to-purple-600 text-white font-semibold py-3 rounded-lg hover:shadow-lg transition-all"
            >
              Create Account
            </button>
          </div>

          <div className="mt-6 text-center">
            <p className="text-gray-600 text-sm">
              Already have an account?{' '}
              <button
                onClick={() => setCurrentView('login')}
                className="text-blue-600 font-semibold hover:underline"
              >
                Sign In
              </button>
            </p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="h-screen flex bg-gray-100">
      {/* Sidebar */}
      <div className={`${showSidebar ? 'w-80' : 'w-0'} bg-white border-r border-gray-200 flex flex-col transition-all duration-300 overflow-hidden`}>
        {/* Sidebar Header */}
        <div className="p-4 bg-gradient-to-r from-blue-600 to-purple-600">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-white rounded-full flex items-center justify-center text-2xl">
                👤
              </div>
              <div className="text-white">
                <div className="font-semibold">{currentUser?.username || 'User'}</div>
                <div className="text-xs opacity-90">Online</div>
              </div>
            </div>
            <button className="text-white hover:bg-white/20 p-2 rounded-lg transition">
              <Menu size={20} />
            </button>
          </div>

          <div className="relative">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" size={18} />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search conversations..."
              className="w-full pl-10 pr-4 py-2 rounded-lg bg-white/20 text-white placeholder-white/70 focus:outline-none focus:bg-white/30"
            />
          </div>
        </div>

        {/* Conversations List */}
        <div className="flex-1 overflow-y-auto">
          <div className="p-2">
            <button className="w-full flex items-center gap-3 p-3 hover:bg-blue-50 rounded-lg transition text-blue-600 font-semibold">
              <UserPlus size={20} />
              <span>Start New Chat</span>
            </button>
          </div>

          {conversations.map((conv) => (
            <div
              key={conv.id}
              onClick={() => setSelectedChat(conv)}
              className={`p-4 border-b border-gray-100 cursor-pointer hover:bg-gray-50 transition ${
                selectedChat?.id === conv.id ? 'bg-blue-50 border-l-4 border-l-blue-600' : ''
              }`}
            >
              <div className="flex items-center gap-3">
                <div className="relative">
                  <div className="w-12 h-12 bg-gradient-to-br from-blue-400 to-purple-400 rounded-full flex items-center justify-center text-2xl">
                    {conv.avatar}
                  </div>
                  {conv.online && (
                    <div className="absolute bottom-0 right-0 w-3 h-3 bg-green-500 rounded-full border-2 border-white"></div>
                  )}
                </div>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center justify-between mb-1">
                    <h3 className="font-semibold text-gray-800 truncate">{conv.name}</h3>
                    <span className="text-xs text-gray-500">{conv.time}</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <p className="text-sm text-gray-600 truncate">{conv.lastMessage}</p>
                    {conv.unread > 0 && (
                      <span className="bg-blue-600 text-white text-xs font-bold px-2 py-1 rounded-full">
                        {conv.unread}
                      </span>
                    )}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Chat Area */}
      <div className="flex-1 flex flex-col">
        {selectedChat ? (
          <>
            {/* Chat Header */}
            <div className="bg-white border-b border-gray-200 p-4 flex items-center justify-between">
              <div className="flex items-center gap-3">
                <button
                  onClick={() => setShowSidebar(!showSidebar)}
                  className="lg:hidden p-2 hover:bg-gray-100 rounded-lg"
                >
                  <Menu size={20} />
                </button>
                <div className="w-10 h-10 bg-gradient-to-br from-blue-400 to-purple-400 rounded-full flex items-center justify-center text-xl">
                  {selectedChat.avatar}
                </div>
                <div>
                  <h2 className="font-semibold text-gray-800">{selectedChat.name}</h2>
                  <p className="text-sm text-gray-500">
                    {selectedChat.online ? 'Active now' : 'Offline'}
                  </p>
                </div>
              </div>
              <div className="flex items-center gap-2">
                <button className="p-2 hover:bg-gray-100 rounded-lg transition">
                  <Phone size={20} className="text-gray-600" />
                </button>
                <button className="p-2 hover:bg-gray-100 rounded-lg transition">
                  <Video size={20} className="text-gray-600" />
                </button>
                <button className="p-2 hover:bg-gray-100 rounded-lg transition">
                  <MoreVertical size={20} className="text-gray-600" />
                </button>
              </div>
            </div>

            {/* Messages Area */}
            <div className="flex-1 overflow-y-auto p-4 bg-gray-50">
              <div className="max-w-4xl mx-auto space-y-4">
                {messages.map((msg) => (
                  <div
                    key={msg.id}
                    className={`flex ${msg.isMine ? 'justify-end' : 'justify-start'}`}
                  >
                    <div
                      className={`max-w-md px-4 py-2 rounded-2xl ${
                        msg.isMine
                          ? 'bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-br-none'
                          : 'bg-white text-gray-800 rounded-bl-none shadow'
                      }`}
                    >
                      {!msg.isMine && (
                        <div className="text-xs font-semibold mb-1 opacity-70">
                          {msg.sender}
                        </div>
                      )}
                      <p className="text-sm leading-relaxed">{msg.text}</p>
                      <div
                        className={`text-xs mt-1 ${
                          msg.isMine ? 'text-white/80' : 'text-gray-500'
                        }`}
                      >
                        {msg.time}
                      </div>
                    </div>
                  </div>
                ))}
                <div ref={messagesEndRef} />
              </div>
            </div>

            {/* Message Input */}
            <div className="bg-white border-t border-gray-200 p-4">
              <div className="max-w-4xl mx-auto flex items-center gap-2">
                <button className="p-2 hover:bg-gray-100 rounded-lg transition">
                  <Paperclip size={20} className="text-gray-600" />
                </button>
                <button className="p-2 hover:bg-gray-100 rounded-lg transition">
                  <Image size={20} className="text-gray-600" />
                </button>
                <input
                  type="text"
                  value={messageInput}
                  onChange={(e) => setMessageInput(e.target.value)}
                  onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
                  placeholder="Type a message..."
                  className="flex-1 px-4 py-2 border border-gray-300 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
                <button className="p-2 hover:bg-gray-100 rounded-lg transition">
                  <Smile size={20} className="text-gray-600" />
                </button>
                <button
                  onClick={handleSendMessage}
                  className="bg-gradient-to-r from-blue-600 to-purple-600 text-white p-3 rounded-full hover:shadow-lg transition"
                >
                  <Send size={20} />
                </button>
              </div>
            </div>
          </>
        ) : (
          <div className="flex-1 flex items-center justify-center bg-gray-50">
            <div className="text-center">
              <MessageCircle size={64} className="text-gray-300 mx-auto mb-4" />
              <h3 className="text-xl font-semibold text-gray-600 mb-2">
                Select a conversation
              </h3>
              <p className="text-gray-500">
                Choose a chat from the sidebar to start messaging
              </p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
