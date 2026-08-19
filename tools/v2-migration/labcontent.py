"""New lab-manual content for Professional Vue.js v2.0 (Vue 3.5 / Vite / Pinia)."""

N  = 'Normal'
H1 = 'Heading 1'
H2 = 'Heading 2'
L  = 'LabNL'
LS = 'LabNL Sub'
LC = 'LabNL Code'
NOTE = 'Note'
CODE = 'Code'
LB = 'LabBullet'

# ---------------------------------------------------------------- front matter
FRONT = [
    (N, 'Version 2.0, 2026'),
    (N, 'by Chris Minnick'),
    (N, 'Copyright 2026, WatzThis?'),
]

# --------------------------------------------------- Setup Instructions (77-107)
SETUP = [
    (H1, 'Setup Instructions'),
    (H2, 'Course Requirements'),
    (N, 'To complete the labs in this course, you will need:'),
    ('List Paragraph', 'A computer running macOS, Windows, or Linux.'),
    ('List Paragraph', 'Access to the Internet.'),
    ('List Paragraph', 'A modern web browser.'),
    ('List Paragraph', 'Ability to install software globally (or certain packages pre-installed as specified below).'),
    (H2, 'Classroom Setup'),
    (N, 'These steps must be completed in advance if the students will not have '
        'administrative access to the computers in the classroom. Otherwise, these '
        'steps can be completed during the course as needed.'),
    (L, 'Install Node.js on each student’s computer.'),
    (LS, 'Go to nodejs.org and download the current LTS release. The labs in this '
         'course require Node.js 20.19 or later, or 22.12 or later — Vite 8 will '
         'refuse to start on anything older.'),
    (L, 'Install a code editor.'),
    (LS, 'We recommend the free Visual Studio Code editor, which you can download '
         'from https://code.visualstudio.com/'),
    (L, 'Make sure a Chromium-based browser (Google Chrome or Microsoft Edge) is '
        'installed, so the Vue DevTools extension is available.'),
    (L, 'Install git on each student’s computer.'),
    (LS, 'If you’re using macOS, you already have git installed. If you’re on '
         'Windows, git can be downloaded from https://git-scm.com. Select all the '
         'default options during installation.'),
    (H2, 'Testing the Setup'),
    (L, 'Open a command prompt.'),
    (LS, 'Use Terminal on macOS (/Applications/Utilities/Terminal).'),
    (LS, 'Use Git Bash, Windows Terminal, or PowerShell on Windows.'),
    (L, 'Check your Node.js version. It must be 20.19+ or 22.12+.'),
    (LC, 'node -v'),
    (L, 'Enter cd to navigate to the user’s home directory (or change to a '
        'directory where student files should be created).'),
    (L, 'Enter the following:'),
    (LC, 'git clone https://github.com/watzthisco/pro-vue'),
    (LS, 'The lab solution files for the course will download into a new directory '
         'called pro-vue.'),
    (L, 'Enter cd pro-vue/setup-test to switch to the test project.'),
    (L, 'Enter npm install'),
    (LS, 'This step will take some time. If it fails, the likely problem is that '
         'your firewall is blocking access to github.com and/or '
         'registry.npmjs.org.'),
    (L, 'When everything is done, enter npm run dev'),
    (LS, 'Vite prints a Local URL (http://localhost:5173/ by default). Open it in '
         'your browser — you should see the starter page.'),
    (L, 'Enter npm run test to confirm that the test runner works as well.'),
    (L, 'If you get an error, delete the node_modules folder (by entering rm -r '
        'node_modules) and run npm install again, followed by npm run dev'),
    (N, ''),
]

# ----------------------------------------------------------- Lab 01 (118-144)
LAB01 = [
    (H1, 'Lab 01 - Installing and Configuring VS Code'),
    (N, 'Visual Studio Code is an integrated development environment for '
        'JavaScript. You can use any code editor or IDE you like, but Visual '
        'Studio Code is open source and has good support for modern frameworks '
        'like Vue.js and Node.js, as well as built-in integrations with the tools '
        'we’ll be using in this course and extensions for doing anything else '
        'you’ll need to do.'),
    (N, ''),
    (N, 'None of the labs in this course (other than this one) will depend on any '
        'particular IDE; so, if you prefer another editor, feel free to use it and '
        'to adapt the instructions in this lab to your own editor.'),
    (N, ''),
    (H2, 'Part 1 - Installing Visual Studio Code'),
    (N, ''),
    (L, 'Go to https://code.visualstudio.com/ .'),
    (L, 'Click the download link.'),
    (N, 'When the download completes, launch the installer and follow the prompts '
        'to install Visual Studio Code.'),
    (N, ''),
    (H2, 'Part 2: Installing Extensions'),
    (N, 'VS Code has thousands of available extensions. To make working with '
        'Vue.js and related JavaScript tools easier, we’ll install a couple of '
        'them now.'),
    (L, 'Click the Extensions icon on the left sidebar.'),
    (L, 'Search for and install the Vue - Official extension, by the Vue core '
        'team. This gives you Vue syntax highlighting, formatting, and type '
        'checking for single-file components.'),
    (NOTE, 'Note: Vue - Official replaces Vetur, which was the Vue 2 extension and '
           'is now deprecated. If you have Vetur installed, disable it — running '
           'both at once causes duplicate errors.'),
    (L, 'Search for and install the ESLint extension, by Microsoft, so lint errors '
        'appear inline as you type.'),
    (H2, 'Part 3: Creating a New Project'),
    (L, 'Start VS Code.'),
    (L, 'Select File > Open Folder, or click the Open Folder link on the start '
        'screen.'),
    (L, 'Select the folder where you want to create your project (such as in '
        'Documents) and click New Folder to create a new folder. Name the new '
        'folder vue-training.'),
    (L, 'Select the new folder and click Open.'),
    (N, ''),
]

# ---------------------------------------------------------- Lab 02 (145-169)
LAB02 = [
    (H1, 'Lab 02: Get Started with Vite'),
    (N, 'Vue projects are scaffolded with create-vue, which builds a project on '
        'top of Vite. Vite serves your source files as native ES modules during '
        'development, so there is no bundling step to wait for when you save a '
        'file.'),
    (NOTE, 'Note: Vue CLI, which earlier versions of this course used, reached end '
           'of life at the end of 2023. create-vue is the tool the Vue '
           'documentation now points to.'),
    (L, 'Start a new project in VS Code (if you didn’t already do this in the '
        'previous lab).'),
    (L, 'Open the terminal (ctrl - `) and scaffold your first app. There is '
        'nothing to install globally — npm create downloads the scaffolding tool '
        'and runs it.'),
    (LC, 'npm create vue@latest conduit'),
    (LS, 'If this produces an error, you most likely need to upgrade the version '
         'of Node.js on your computer (see the setup instructions).'),
    (L, 'Answer the prompts. For this course, answer No to every optional feature '
        'except Vitest, which we will use in Lab 05:'),
    (LC, 'TypeScript?                       No'),
    (LC, 'JSX Support?                      No'),
    (LC, 'Vue Router?                       No'),
    (LC, 'Pinia?                            No'),
    (LC, 'Vitest for Unit Testing?          Yes'),
    (LC, 'End-to-End Testing?               No'),
    (LC, 'ESLint for code quality?          Yes'),
    (LS, 'We add Vue Router and Pinia by hand later in the course, so you can see '
         'exactly what each one contributes.'),
    (L, 'Go into the new directory and install the dependencies.'),
    (LC, 'cd conduit'),
    (LC, 'npm install'),
    (L, 'Test that everything was installed and works.'),
    (LC, 'npm run dev'),
    (L, 'When the server is ready, Vite prints a Local URL. Open it in a web '
        'browser (http://localhost:5173/ by default).'),
    (LS, 'If the app was successfully created, you should see the create-vue '
         'welcome page.'),
    (L, 'In your code editor, find App.vue inside the src directory and open it '
        'for editing.'),
    (L, 'Change some of the text in the <template> section.'),
    (L, 'Return to your web browser and notice that the page updates without a '
        'reload. This is hot module replacement.'),
    (LS, 'If it doesn’t update, return to your terminal and check that npm run '
         'dev is still running.'),
    (L, 'Have a look at the project Vite created. Two things differ from the '
        'Vue CLI layout you may have seen before:'),
    (LS, 'index.html is in the project root, not in public/. It is the entry point '
         'of the app, and it loads /src/main.js with a <script type="module"> tag.'),
    (LS, 'vite.config.js replaces vue.config.js. It is a plain ES module that '
         'exports a configuration object.'),
    (N, ''),
]

# ---------------------------------------------------------- Lab 03 (177-290)
LAB03 = [
    (H1, 'Lab 03: Your First Component'),
    (N, 'Vue.js components let you divide your user interface into independent and '
        'reusable pieces. The simplest components just output some HTML, given '
        'some input.'),
    (N, ''),
    (N, 'In this lab, you’ll create a component to hold the contents of the page '
        'header.'),
    (L, 'Create a new file named Header.vue in the src/components directory.'),
    (LS, 'This component will hold the navigation and logo for our app. At this '
         'point it will just render static HTML. We’ll be using the Bootstrap CSS '
         'framework to style the navigation as a responsive horizontal navbar.'),
    (L, 'Inside Header.vue create a script element with the setup attribute, and a '
        'template element:'),
    (LC, '<script setup>'),
    (LC, '</script>'),
    (LC, ''),
    (LC, '<template>'),
    (LC, '</template>'),
    (LS, 'The setup attribute is what makes this a Composition API component. '
         'Everything you declare at the top level of <script setup> — imports, '
         'variables, functions — is available in the template automatically. '
         'There is no export default and no components object to maintain.'),
    (NOTE, 'Note: <script setup> is compile-time syntax, not a runtime API. The '
           'Vue compiler turns it into a normal component definition. The '
           'component’s name comes from the file name, which is why Header.vue '
           'can be used as <Header /> without registering it.'),
    (L, 'Inside the template element, create a nav element containing a div '
        'element, and give the div element a class of container. The container '
        'class will cause Bootstrap to style the contents of the nav element as a '
        'responsive container.'),
    (LC, '<template>'),
    (LC, '  <nav>'),
    (LC, '    <div class="container">'),
    (LC, '    </div>'),
    (LC, '  </nav>'),
    (LC, '</template>'),
    (L, 'Give the nav element the Bootstrap navbar class.'),
    (LC, '<nav class="navbar">'),
    (L, 'Make a logo link in the container by creating a link and giving it the '
        'navbar-brand class.'),
    (LC, '<div class="container">'),
    (LC, '  <a href="/" class="navbar-brand">Conduit</a>'),
    (LC, '</div>'),
    (L, 'Below the logo link create a list using a ul element and several li '
        'elements.'),
    (LC, '<ul>'),
    (LC, '  <li>Home</li>'),
    (LC, '  <li>Sign In</li>'),
    (LC, '  <li>Sign Up</li>'),
    (LC, '</ul>'),
    (L, 'Add Bootstrap’s nav and navbar-nav classes to the ul to format it as a '
        'navbar, and add the flex-row class to make it a horizontal navbar.'),
    (LC, '<ul class="nav navbar-nav flex-row">'),
    (L, 'Add nav-item classes to each of the li elements, and add p-2 to add some '
        'padding around each item.'),
    (LC, '<li class="nav-item p-2">Home</li>'),
    (L, 'Turn the text in each nav-item into a link and add the nav-link class.'),
    (LC, '<li class="nav-item p-2">'),
    (LC, '  <a class="nav-link">Home</a>'),
    (LC, '</li>'),
    (L, 'When it’s done, Header.vue should look like this:'),
    (LC, '<script setup>'),
    (LC, '// A purely presentational component: no state, no props, no events.'),
    (LC, '</script>'),
    (LC, ''),
    (LC, '<template>'),
    (LC, '  <nav class="navbar">'),
    (LC, '    <div class="container">'),
    (LC, '      <a href="/" class="navbar-brand">Conduit</a>'),
    (LC, '      <ul class="nav navbar-nav flex-row">'),
    (LC, '        <li class="nav-item p-2">'),
    (LC, '          <a class="nav-link">Home</a>'),
    (LC, '        </li>'),
    (LC, '        <li class="nav-item p-2">'),
    (LC, '          <a class="nav-link">Sign In</a>'),
    (LC, '        </li>'),
    (LC, '        <li class="nav-item p-2">'),
    (LC, '          <a class="nav-link">Sign Up</a>'),
    (LC, '        </li>'),
    (LC, '      </ul>'),
    (LC, '    </div>'),
    (LC, '  </nav>'),
    (LC, '</template>'),
    (L, 'Open App.vue. If it still contains the create-vue welcome page, delete '
        'everything in it and start from this:'),
    (LC, '<script setup>'),
    (LC, 'import HelloWorld from \'./components/HelloWorld.vue\';'),
    (LC, '</script>'),
    (LC, ''),
    (LC, '<template>'),
    (LC, '  <div id="app">'),
    (LC, '    <HelloWorld msg="Vue.js is fun!" />'),
    (LC, '  </div>'),
    (LC, '</template>'),
    (L, 'Import Header at the top of the <script setup> block in App.vue.'),
    (LC, 'import Header from \'./components/Header.vue\';'),
    (LS, 'That import is all that is required. Under the Options API you also had '
         'to list the component in a components object; with <script setup> the '
         'import itself registers it.'),
    (NOTE, 'Note: include the .vue file extension in the import. Vite resolves '
           'extensionless imports for .js and .mjs only, so \'./components/Header\' '
           'will fail where Vue CLI used to accept it.'),
    (L, 'Add <Header /> inside the <template> in App.vue, above the HelloWorld '
        'component.'),
    (L, 'Delete the contents of the <style> element in App.vue, if there is one.'),
    (L, 'Open index.html — it is in the project root, not in public/.'),
    (L, 'In your browser, go to https://getbootstrap.com/docs/5.3/getting-started/'
        'introduction/. Copy the Bootstrap CSS <link> element and paste it into the '
        'head element in index.html.'),
    (LC, '<link'),
    (LC, '  href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"'),
    (LC, '  rel="stylesheet"'),
    (LC, '  crossorigin="anonymous"'),
    (LC, '/>'),
    (L, 'Copy the Bootstrap bundle <script> tag into index.html, right above the '
        '</body> tag.'),
    (NOTE, 'Note: Bootstrap 5 dropped its jQuery dependency, so — unlike Bootstrap '
           '4 — there is no jQuery script tag to add.'),
    (L, 'Start the app (if it’s not already running) with npm run dev, and view it '
        'in your browser.'),
    (N, ''),
]

# ---------------------------------------------------------- Lab 05 (357-388)
LAB05 = [
    (H1, 'Lab 05: Testing Vue'),
    (N, 'In this lab, you’ll create simple unit tests for each of the components '
        'you’ve made so far. If you answered Yes to the Vitest prompt in Lab 02, '
        'the test runner is already installed. Vitest shares Vite’s configuration '
        'and transform pipeline, so your tests resolve imports and .vue files '
        'exactly the way your app does.'),
    (L, 'Make a new directory (at the same level as the src directory) and name it '
        'tests.'),
    (L, 'Make a subdirectory of your tests directory and name it components.'),
    (L, 'Make a new file in this directory named Header.spec.js.'),
    (L, 'Import the test functions from vitest, and mount from Vue Test Utils.'),
    (LC, 'import { describe, expect, it } from \'vitest\';'),
    (LC, 'import { mount } from \'@vue/test-utils\';'),
    (NOTE, 'Note: this course uses Vue Test Utils 2, which is the version built for '
           'Vue 3. Its API differs from version 1 in a few places — most visibly, '
           'the propsData mounting option is now called props, and createLocalVue '
           'is gone in favour of the global.plugins option.'),
    (L, 'Import the Header component. The @ alias points at src, and is configured '
        'in vite.config.js.'),
    (LC, 'import Header from \'@/components/Header.vue\';'),
    (L, 'Write a function to mount the component.'),
    (LC, 'const createWrapper = () => mount(Header);'),
    (L, 'Write a describe function to describe your test suite.'),
    (LC, 'describe(\'Header\', () => {'),
    (LC, '});'),
    (L, 'Inside the describe function, create a test.'),
    (LC, '  it(\'should render without a problem\', () => {'),
    (LC, '    const wrapper = createWrapper();'),
    (LC, ''),
    (LC, '    expect(wrapper.exists()).toBe(true);'),
    (LC, '  });'),
    (L, 'Open vite.config.js and confirm it has a test section. If it does not, '
        'add one — Vitest needs a DOM implementation to mount components into.'),
    (LC, 'test: {'),
    (LC, '  environment: \'jsdom\','),
    (LC, '  globals: true,'),
    (LC, '  include: [\'tests/**/*.spec.js\'],'),
    (LC, '},'),
    (L, 'If jsdom isn’t installed yet, install it.'),
    (LC, 'npm install --save-dev jsdom'),
    (L, 'Run npm run test to check whether it works.'),
    (L, 'Make copies of this spec for the Home component and the Footer '
        'component.'),
    (L, 'Modify the contents of the new files to test the new components.'),
    (L, 'Run your tests again and make sure that all of them pass.'),
    (L, 'Try npm run test:watch. Vitest re-runs only the tests affected by the '
        'file you just saved.'),
    (N, ''),
]

# ---------------------------------------------------- Lab 08 body (494-499)
LAB08_CODE = [
    (L, 'Enter the following code inside of server.js'),
    (LC, 'import http from \'node:http\';\n'
         '\n'
         'const hostname = \'127.0.0.1\';\n'
         'const port = 3000;\n'
         '\n'
         'const server = http.createServer((req, res) => {\n'
         '    res.statusCode = 200;\n'
         '    res.setHeader(\'Content-Type\', \'text/plain\');\n'
         '    res.end(\'Hello World\\n\');\n'
         '});\n'
         '\n'
         'server.listen(port, hostname, () => {\n'
         '    console.log(`Server running at http://${hostname}:${port}/`);\n'
         '});'),
    (NOTE, 'Note: the console.log statement uses a template literal to combine '
           'dynamic values with static text. The characters surrounding the string '
           'are backticks (upper left of the keyboard), not single quotes.'),
    (NOTE, 'Note: node: prefixes such as node:http identify built-in modules '
           'explicitly, so they can never be shadowed by a package of the same '
           'name from npm.'),
    (L, 'Because this file uses import rather than require, Node needs to treat it '
        'as an ES module. Create a package.json alongside it containing:'),
    (LC, '{ "type": "module" }'),
    (L, 'Save the server.js file.'),
    (L, 'In your terminal, navigate to the labs/lab08 folder and run the program by '
        'typing:'),
    (LC, 'node server.js'),
]

# --------------------------------------------------------- Lab 09 (506-583)
LAB09 = [
    (H1, 'Lab 09 - Automate Linting'),
    (N, 'Linting is a way to perform static code analysis on your files. Static '
        'code analysis looks at the syntax (and the style, in some cases) of your '
        'JavaScript and alerts you if there are problems.'),
    (N, ''),
    (N, 'In this lab, you will install ESLint and use it to check a JavaScript '
        'file.'),
    (NOTE, 'Note: ESLint 9 introduced a new configuration format called flat '
           'config. The old .eslintrc.js format, and the --ext flag that went with '
           'it, were removed in ESLint 10. Configuration now lives in a file named '
           'eslint.config.js that exports an array.'),
    (L, 'If your terminal program isn’t already open, open it and go to '
        'labs/lab09.'),
    (L, 'Install ESLint and the two packages the config file will import.'),
    (LC, 'npm install --save-dev eslint @eslint/js globals'),
    (L, 'Create a file named eslint.config.js in the root of the directory.'),
    (L, 'Import the recommended rule set and the standard global definitions.'),
    (LC, 'import js from \'@eslint/js\';'),
    (LC, 'import globals from \'globals\';'),
    (L, 'Export an array. Each object in the array is a configuration that applies '
        'to the files it matches; later objects override earlier ones.'),
    (LC, 'export default ['),
    (LC, '];'),
    (L, 'Add an ignores entry as the first element. In flat config this replaces '
        'the .eslintignore file, which ESLint 10 no longer reads.'),
    (LC, '  {'),
    (LC, '    ignores: [\'node_modules/**\', \'eslint.config.js\'],'),
    (LC, '  },'),
    (L, 'Add ESLint’s recommended rules.'),
    (LC, '  js.configs.recommended,'),
    (L, 'Add a configuration object for your own source files, with the language '
        'options and the style rules you want to enforce.'),
    (LC, '  {'),
    (LC, '    files: [\'**/*.js\'],'),
    (LC, '    languageOptions: {'),
    (LC, '      ecmaVersion: \'latest\','),
    (LC, '      sourceType: \'module\','),
    (LC, '      globals: {'),
    (LC, '        ...globals.browser,'),
    (LC, '      },'),
    (LC, '    },'),
    (LC, '    rules: {'),
    (LC, '      indent: [\'error\', 4],'),
    (LC, '      \'linebreak-style\': [\'error\', \'unix\'],'),
    (LC, '      quotes: [\'error\', \'single\'],'),
    (LC, '      semi: [\'error\', \'always\'],'),
    (LC, '      \'no-console\': \'warn\','),
    (LC, '    },'),
    (LC, '  },'),
    (LS, 'Adjust indent, quotes and linebreak-style to match your own preferences. '
         'If you’re on Windows you may want linebreak-style set to \'windows\'.'),
    (LS, 'no-console is set to warn rather than error because we use console.log '
         'in later labs.'),
    (L, 'Create a new script in package.json called lint. Note that there is no '
        '--ext flag: flat config decides which files to lint through the files '
        'property.'),
    (LC, '"lint": "eslint .",'),
    (LS, 'I recommend putting it before the "test" script.'),
    (L, 'Run npm run lint.'),
    (L, 'Fix the errors reported by ESLint, or adjust eslint.config.js to fit your '
        'desired coding style, until only the no-console warning remains.'),
    (L, 'Make the lint script run prior to the test script in the prebuild '
        'script.'),
    (N, ''),
]

# --------------------------------------------------------- Lab 10 (584-618)
LAB10 = [
    (H1, 'Lab 10: Manual In-Browser Testing and Debugging'),
    (N, ''),
    (N, 'In this lab, you will get acquainted with your browser’s developer tools '
        'for inspecting and debugging your front-end code.'),
    (N, ''),
    (L, 'In your terminal, navigate to the conduit folder you were working with in '
        'labs 01-05.'),
    (L, 'Enter npm run dev to start the Vite development server.'),
    (L, 'Install the Vue DevTools browser extension from '
        'https://devtools.vuejs.org/guide/installation.'),
    (LS, 'Vite projects can also run the DevTools in-page, without a browser '
         'extension, by installing the vite-plugin-vue-devtools package. Either '
         'approach works for this lab.'),
    (L, 'Restart your browser, then go to http://localhost:5173.'),
    (L, 'Press Command-Option-I (on macOS) or Ctrl-Shift-I (Windows) to open the '
        'Developer Tools.'),
    (L, 'Dock the Developer Tools to the right side by clicking the Customize '
        'button on the right side of the Developer Tools toolbar and selecting '
        'Dock Right.'),
    (N, ''),
    (LB, 'Click Elements. The current HTML and CSS of your document (as it exists '
         'in the DOM) will appear.'),
    (LB, 'Expand the <div id="app"> element and click on one of the elements '
         'inside it.'),
    (LB, 'In the styles pane, add border: 10px solid red; to the element.style '
         'object.'),
    (LB, 'Right-click an h1 element and select Hide element.'),
    (LB, 'Click the Console tab to open the JavaScript console.'),
    (NOTE, 'You can also open the JavaScript console at any time by pressing '
           'Ctrl-Shift-J (Windows) or Command-Option-J (Mac).'),
    (LB, 'Enter the following into the console, followed by Return (or Enter):'),
    (CODE, 'document.body.innerHTML = \'<h1>Here is some new text!</h1>\';'),
    (N, 'The content of the document’s body element will change to the HTML you '
        'just entered.'),
    (LB, 'Click the Sources tab.'),
    (N, ''),
    (N, 'The JavaScript debugger will open.'),
    (N, ''),
    (LB, 'Vite serves your source files unbundled during development, so you can '
         'find src/App.vue and src/components/Header.vue in the file tree exactly '
         'as they are on disk. Open one and click a line number to set a '
         'breakpoint.'),
    (LB, 'Refresh the page.'),
    (N, ''),
    (N, 'Execution of the script will halt prior to the statement running. Examine '
        'the different options available and hover over the buttons to find out '
        'what they do.'),
    (N, ''),
    (LB, 'Click the Vue tab that the DevTools extension added. Select a component '
         'in the tree and inspect its props and state in the right-hand pane.'),
    (N, ''),
]

# --------------------------------------------------- Lab 11 script blocks
LAB11_SCRIPTS = [
    (L, 'Make a new component named GlobalFeed. This will contain the list of '
        'articles that will display for logged-out users. Use the following:'),
    (LC, '<script setup>'),
    (LC, 'import ArticleList from \'./ArticleList.vue\';'),
    (LC, '</script>'),
    (LC, ''),
    (LC, '<template>'),
    (LC, '  <div class="home-global"><ArticleList type="all" /></div>'),
    (LC, '</template>'),
    (LS, 'The import both brings ArticleList into scope and registers it for the '
         'template. There is no components object to maintain.'),
    (L, 'Make a component named ArticleList. This will display a list of article '
        'previews. Use this template:'),
    (LC, '<template>'),
    (LC, '  <div>'),
    (LC, '    <div v-if="articles.length === 0" class="article-preview">'),
    (LC, '      No articles are here... yet.'),
    (LC, '    </div>'),
    (LC, '    <ArticlePreview'),
    (LC, '      v-for="(article, index) in articles"'),
    (LC, '      :key="article.title + index"'),
    (LC, '      :article="article"'),
    (LC, '    />'),
    (LC, '  </div>'),
    (LC, '</template>'),
    (LS, 'This template uses the v-if directive to check whether there are any '
         'articles to display. It then uses v-for to output an ArticlePreview '
         'component for each article.'),
    (LS, 'We pass a prop, article, into each ArticlePreview, and a key so Vue can '
         'track list items across re-renders.'),
    (NOTE, 'Note: in Vue 3, :key goes on the element that carries v-for. In Vue 2 '
           'you could not use key on a <template v-for>; in Vue 3 that is the '
           'required place for it.'),
    (L, 'Start the script block by importing the ArticlePreview component (which '
        'we’ll create in a moment):'),
    (LC, '<script setup>'),
    (LC, 'import ArticlePreview from \'./ArticlePreview.vue\';'),
    (LC, '</script>'),
    (L, 'Copy articles.json from the labs/lab11 folder into a subfolder of src '
        'named json. This file contains our article data (until we start using a '
        'web API in a later lab).'),
    (L, 'Import articles.json and ref into ArticleList.'),
    (LC, 'import { ref } from \'vue\';'),
    (LC, 'import articlesJson from \'../json/articles.json\';'),
    (L, 'Declare the component’s state. ref() is the Composition API replacement '
        'for the data() function: it wraps a value in a reactive container.'),
    (LC, 'const articles = ref(articlesJson);'),
    (LS, 'Inside <script setup> you read and write a ref through its .value '
         'property. In the template, Vue unwraps it for you, which is why the '
         'template above says articles.length and not articles.value.length.'),
    (L, 'Make a component named ArticlePreview. This will determine how each '
        'preview looks and will eventually contain a link to the full article. '
        'Use this template:'),
    (LC, '<template>'),
    (LC, '  <div class="article-preview">'),
    (LC, '    <h1 v-text="article.title" />'),
    (LC, '    <p v-text="article.description" />'),
    (LC, '    <span>Read more...</span>'),
    (LC, '  </div>'),
    (LC, '</template>'),
    (L, 'ArticlePreview receives a prop, article, from its parent component. '
        'Declare it with the defineProps compiler macro.'),
    (LC, '<script setup>'),
    (LC, 'defineProps({'),
    (LC, '  article: { type: Object, required: true },'),
    (LC, '});'),
    (LC, '</script>'),
    (NOTE, 'Note: defineProps, defineEmits and defineExpose are compiler macros. '
           'They are not imported from anywhere and they only work at the top '
           'level of <script setup>.'),
    (L, 'Import the GlobalFeed component into the Home component, and replace the '
        '<p>Home Content Placeholder</p> in its template with <GlobalFeed />.'),
    (L, 'Run npm run dev and preview your application in your browser.'),
    (N, ''),
]

# ------------------------------------------------- Lab 13 (767-792) computed
LAB13 = [
    (H1, 'Lab 13: Computed Properties'),
    (N, 'In this lab, you’ll use a computed property to add links to each '
        'article’s preview.'),
    (N, ''),
    (L, 'Open the ArticlePreview component in your code editor.'),
    (L, 'Import computed from vue, and capture the return value of defineProps so '
        'you can read the props from JavaScript.'),
    (LC, 'import { computed } from \'vue\';'),
    (LC, ''),
    (LC, 'const props = defineProps({'),
    (LC, '  article: { type: Object, required: true },'),
    (LC, '});'),
    (LS, 'In the template you write article directly. In the script block you have '
         'to go through the object defineProps returns, hence props.article.'),
    (L, 'Create a computed property called articleLink, which returns the "slug" '
        '(or path) to the current article.'),
    (LC, 'const articleLink = computed(() => ({ slug: props.article.slug }));'),
    (LS, 'computed() returns a read-only ref. Like a computed option in the '
         'Options API it is cached, and only re-evaluates when one of the '
         'reactive values it read has changed.'),
    (L, 'Use the v-bind shorthand in the ArticlePreview template to link the "Read '
        'more..." text to the article slug.'),
    (LC, '<span><a :href="articleLink.slug">Read more...</a></span>'),
    (L, 'Challenge: add a second computed property that formats the article’s '
        'createdAt date for display.'),
    (N, ''),
]

# ---------------------------------------------------- Lab 14 (793-802) state
LAB14 = [
    (H1, 'Lab 14: Methods and State'),
    (N, 'In this lab, you’ll create a "favorite" button associated with each '
        'article preview, which can be toggled on and off. The state of the '
        'button is held in a ref, and it is changed by a plain function.'),
    (L, 'Import ref into ArticlePreview and declare a boolean named favorited.'),
    (LC, 'import { ref } from \'vue\';'),
    (LC, ''),
    (LC, 'const favorited = ref(false);'),
    (LS, 'A ref declared inside a component is created fresh for every instance of '
         'that component, so each article preview gets its own favorited value. '
         'This is what the data() function guaranteed under the Options API.'),
    (L, 'Create a function inside ArticlePreview named toggleFavorite() that flips '
        'the value of favorited. Remember the .value.'),
    (LC, 'function toggleFavorite() {'),
    (LC, '  favorited.value = !favorited.value;'),
    (LC, '}'),
    (LS, 'There is no methods object. Any function declared at the top level of '
         '<script setup> is available to the template.'),
    (L, 'Make a button inside the ArticlePreview template that calls '
        'toggleFavorite() when it’s clicked and updates its colour, text, or icon '
        'based on the value of favorited.'),
    (LC, '<button'),
    (LC, '  class="btn btn-sm float-end"'),
    (LC, '  :class="{'),
    (LC, '    \'btn-primary\': favorited,'),
    (LC, '    \'btn-outline-primary\': !favorited,'),
    (LC, '  }"'),
    (LC, '  @click="toggleFavorite"'),
    (LC, '>'),
    (LC, '  <i class="ion-heart"></i>'),
    (LC, '</button>'),
    (NOTE, 'Note: float-end is the Bootstrap 5 name for what Bootstrap 4 called '
           'float-right. The same rename applies to text-start / text-end.'),
    (L, 'Challenge: add a favoritesCount ref and display it on the button, so it '
        'tracks how many times the button for an article has been clicked.'),
    (N, ''),
]

# --------------------------------------------------------- Lab 15 (803-828)
LAB15 = [
    (H1, 'Lab 15: Events'),
    (N, 'In this lab, you’ll add a font-size control to the ArticleList component '
        'that controls the font size of all the article preview instances.'),
    (N, ''),
    (L, 'Add a ref to the ArticleList component called articleFontSize with a '
        'value of 1.'),
    (LC, 'const articleFontSize = ref(1);'),
    (L, 'Pass the value of articleFontSize into the ArticlePreview component by '
        'binding the style attribute:'),
    (LC, '<ArticlePreview'),
    (LC, '  :style="{ fontSize: articleFontSize + \'em\' }"'),
    (LC, '  ...'),
    (LC, '/>'),
    (L, 'Start the development server (npm run dev) and try changing the initial '
        'value to 3. You should see the article text get larger.'),
    (L, 'Set articleFontSize back to 1.'),
    (L, 'In ArticlePreview, declare the events this component can raise using the '
        'defineEmits macro.'),
    (LC, 'const emit = defineEmits([\'enlarge-text\']);'),
    (NOTE, 'Note: declaring events matters more in Vue 3 than it did in Vue 2. Any '
           'listener that is not declared here falls through to the component’s '
           'root element as a native DOM attribute, which is rarely what you want '
           'for a custom event.'),
    (L, 'Create a button inside the ArticlePreview template that emits the '
        'enlarge-text event on click.'),
    (LC, '<button @click="emit(\'enlarge-text\', 0.1)">Enlarge Text</button>'),
    (LS, 'In the Options API you would have written $emit here. With <script '
         'setup> you call the function that defineEmits returned.'),
    (L, 'Listen for the enlarge-text event in the ArticleList component and '
        'increase the value of articleFontSize by 0.1 when it’s received.'),
    (LC, '<ArticlePreview'),
    (LC, '  :style="{ fontSize: articleFontSize + \'em\' }"'),
    (LC, '  @enlarge-text="articleFontSize += 0.1"'),
    (LC, '/>'),
    (L, 'Add another button named "Shrink Text" and make it work.'),
    (L, 'Challenge: make clicking the button only affect the article description, '
        'not the text of the button itself.'),
    (N, ''),
]

# --------------------------------------------------------- Lab 16 (829-899)
LAB16 = [
    (H1, 'Lab 16: Component Lifecycle'),
    (N, 'In this lab, you’ll load the articles from a web API when the component '
        'is mounted.'),
    (L, 'Create a folder inside src named common and create a file in it named '
        'config.js'),
    (L, 'Inside config.js, export a const named API_URL containing the URL of the '
        'public API we’ll be replacing our articles.json file with. Reading it '
        'from an environment variable lets a class point at a different server '
        'without editing code.'),
    (LC, 'export const API_URL ='),
    (LC, '  import.meta.env.VITE_API_URL ?? \'https://api.realworld.io/api\';'),
    (NOTE, 'Note: Vite exposes environment variables on import.meta.env, and only '
           'those whose names begin with VITE_. Create a .env.local file in the '
           'project root to override it. process.env is not available in browser '
           'code.'),
    (L, 'Export API_URL as the default export for config.js.'),
    (LC, 'export default API_URL;'),
    (L, 'Install axios.'),
    (LC, 'npm install axios'),
    (NOTE, 'Note: earlier versions of this course also installed vue-axios, a '
           'plugin that hung axios off the global Vue object as Vue.axios. Vue 3 '
           'has no global Vue object — each app created with createApp() is '
           'isolated — so instead we create a configured axios instance and import '
           'it wherever it is needed. That is a plain ES module, which is easier '
           'to test and to reason about.'),
    (L, 'Create a file in src/common named api.service.js and import axios and '
        'API_URL into it.'),
    (LC, 'import axios from \'axios\';'),
    (LC, ''),
    (LC, 'import { API_URL } from \'@/common/config\';'),
    (L, 'Create the axios instance that every request will go through.'),
    (LC, 'const client = axios.create({ baseURL: API_URL });'),
    (L, 'Create a const named ApiService, holding an object with an init() method.'),
    (LC, 'const ApiService = {'),
    (LC, '  init() {'),
    (LC, '    client.defaults.baseURL = API_URL;'),
    (LC, '  },'),
    (LC, '};'),
    (L, 'Export ApiService.'),
    (LC, 'export default ApiService;'),
    (L, 'Import ApiService into main.js and call init() before mounting the app.'),
    (LC, 'import ApiService from \'./common/api.service\';'),
    (LC, ''),
    (LC, 'ApiService.init();'),
    (LC, ''),
    (LC, 'createApp(App).mount(\'#app\');'),
    (L, 'Add a query method to the ApiService object in api.service.js'),
    (LC, '  query(resource, params) {'),
    (LC, '    return client.get(resource, params).catch((error) => {'),
    (LC, '      throw new Error(`[RWV] ApiService ${error}`);'),
    (LC, '    });'),
    (LC, '  },'),
    (L, 'Import ApiService and onMounted into ArticleList.vue'),
    (LC, 'import { onMounted, ref } from \'vue\';'),
    (LC, ''),
    (LC, 'import ApiService from \'../common/api.service\';'),
    (L, 'Write a fetchArticles function that uses the query method.'),
    (LC, 'async function fetchArticles() {'),
    (LC, '  const { data } = await ApiService.query(\'articles\');'),
    (LC, ''),
    (LC, '  return data.articles;'),
    (LC, '}'),
    (L, 'Call fetchArticles() from the onMounted lifecycle hook and assign the '
        'result to the articles ref.'),
    (LC, 'onMounted(async () => {'),
    (LC, '  articles.value = await fetchArticles();'),
    (LC, '});'),
    (LS, 'onMounted is the Composition API equivalent of the mounted option. The '
         'hooks are all imported from vue and registered by calling them inside '
         '<script setup>: onBeforeMount, onMounted, onBeforeUpdate, onUpdated, '
         'onBeforeUnmount and onUnmounted.'),
    (NOTE, 'Note: Vue 2’s beforeDestroy and destroyed hooks were renamed to '
           'onBeforeUnmount and onUnmounted in Vue 3. There is no onCreated hook — '
           'the body of <script setup> is the created hook.'),
    (L, 'Remove the articles.json import from ArticleList.vue and initialise '
        'articles to an empty array.'),
    (LC, 'const articles = ref([]);'),
    (LS, 'Start it as an array, not an object: the template calls '
         'articles.length, which is undefined on a plain object and would make '
         'the "No articles..." message never appear.'),
    (L, 'Make sure the development server is running and refresh your page. The '
        'articles should now come from the API.'),
    (L, 'Challenge: fix the footer so that it sticks to the bottom of the list of '
        'articles when the list is populated.'),
    (N, ''),
]

# --------------------------------------------------------- Lab 17 (900-935)
LAB17 = [
    (H1, 'Lab 17: Forms'),
    (N, 'In this lab, you’ll implement an input box that filters the currently '
        'displayed list of articles based on the text entered into it.'),
    (L, 'Create an input in the ArticleList component and bind it with v-model.'),
    (LC, '<input'),
    (LC, '  v-model="searchDetails"'),
    (LC, '  class="form-control"'),
    (LC, '  placeholder="filter articles"'),
    (LC, '/>'),
    (NOTE, 'Note: the earlier version of this lab used v-model.number. That '
           'modifier casts the input to a number, which is wrong here — we are '
           'filtering on text. Leave it off.'),
    (L, 'Add a ref named searchDetails to hold the search text.'),
    (LC, 'const searchDetails = ref(\'\');'),
    (L, 'Import computed and make a computed property in ArticleList called '
        'filterIt.'),
    (LC, 'const filterIt = computed(() =>'),
    (LC, '  articles.value.filter((article) =>'),
    (LC, '    article.title.includes(searchDetails.value),'),
    (LC, '  ),'),
    (LC, ');'),
    (LS, 'Both refs are read with .value inside the computed callback. Because '
         'this is an arrow function there is no this to capture, so the "var self '
         '= this" trick the Options API version needed is gone.'),
    (L, 'Modify the v-for directive in ArticleList.vue to use filterIt instead of '
        'articles:'),
    (LC, 'v-for="(article, index) in filterIt"'),
    (L, 'Start up your development server and try typing letters into the search '
        'form to see how the list is filtered.'),
    (L, 'Challenge: make the search case-insensitive.'),
    (L, 'Challenge: make the search consider the description text as well as the '
        'title.'),
    (N, ''),
]

# ------------------------------------------------------ Lab 19 (940-945)
LAB19 = [
    (H1, 'Lab 19: Composables'),
    (N, 'A composable is a function that uses the Composition API to encapsulate '
        'and reuse stateful logic. Composables are what Vue 3 offers in place of '
        'mixins.'),
    (NOTE, 'Note: mixins still work in Vue 3, but the documentation marks them as '
           'legacy. Their problems are that the source of an inherited property '
           'is invisible at the point of use, that name collisions between mixins '
           'are resolved silently, and that a mixin cannot take parameters. A '
           'composable has none of these problems: you pass its inputs in and you '
           'name its outputs on the way out.'),
    (L, 'Make a directory inside src named composables.'),
    (L, 'Create a file in it named useArticleFilter.js'),
    (LS, 'By convention a composable is named use followed by what it does, and '
         'lives in its own file.'),
    (L, 'Export a function that takes the list of articles as an argument and '
        'returns the search text and the filtered list.'),
    (LC, 'import { computed, ref } from \'vue\';'),
    (LC, ''),
    (LC, 'export function useArticleFilter(articles) {'),
    (LC, '  const searchDetails = ref(\'\');'),
    (LC, ''),
    (LC, '  const filterIt = computed(() =>'),
    (LC, '    (articles.value ?? []).filter((article) =>'),
    (LC, '      article.title.includes(searchDetails.value),'),
    (LC, '    ),'),
    (LC, '  );'),
    (LC, ''),
    (LC, '  return { searchDetails, filterIt };'),
    (LC, '}'),
    (LS, 'Note that articles arrives as a ref, so the composable reads it through '
         '.value and stays reactive to changes made by the caller.'),
    (L, 'Use the composable in ArticleList.vue, and delete the local searchDetails '
        'ref and filterIt computed property.'),
    (LC, 'import { useArticleFilter } from \'../composables/useArticleFilter\';'),
    (LC, ''),
    (LC, 'const { searchDetails, filterIt } = useArticleFilter(articles);'),
    (L, 'Confirm the filter still works in the browser.'),
    (L, 'Challenge: implement filtering of the tags in the right column, reusing '
        'the same composable.'),
    (N, ''),
]

# ------------------------------------------------------- Lab 20 (946-1109)
LAB20 = [
    (H1, 'Lab 20: Implementing Pinia'),
    (N, 'In this lab, you’ll convert the Conduit application to use a centralized '
        'store with Pinia.'),
    (NOTE, 'Note: earlier versions of this course used Vuex. Vuex is now in '
           'maintenance mode and Pinia is the officially recommended store for '
           'Vue. The concepts carry over almost one for one — state and getters '
           'keep their names, and actions absorb what Vuex split between actions '
           'and mutations. Pinia has no mutations at all: an action assigns to '
           'state directly. It also drops the string action-type constants and '
           'the dispatch/commit indirection, so a store method is called like an '
           'ordinary function and can be type-checked and jumped to in an '
           'editor.'),
    (L, 'Install Pinia.'),
    (LC, 'npm install pinia'),
    (L, 'Import createPinia in main.js and install it on the app.'),
    (LC, 'import { createApp } from \'vue\';'),
    (LC, 'import { createPinia } from \'pinia\';'),
    (LC, ''),
    (LC, 'const app = createApp(App);'),
    (LC, ''),
    (LC, 'app.use(createPinia());'),
    (LC, 'app.mount(\'#app\');'),
    (LS, 'Unlike a Vuex store, a Pinia instance holds no state of its own. Each '
         'store is defined in its own file and registers itself the first time it '
         'is used.'),
    (L, 'Make a new directory in src named stores.'),
    (L, 'Make a new file, home.js, inside stores.'),
    (L, 'Make a new API service in api.service.js called ArticlesService.'),
    (LC, 'export const ArticlesService = {'),
    (LC, '  query(type, params) {'),
    (LC, '    return ApiService.query(`articles${type === \'feed\' ? \'/feed\' : \'\'}`, {'),
    (LC, '      params,'),
    (LC, '    });'),
    (LC, '  },'),
    (LC, '};'),
    (L, 'Import defineStore and ArticlesService into stores/home.js'),
    (LC, 'import { defineStore } from \'pinia\';'),
    (LC, ''),
    (LC, 'import { ArticlesService } from \'@/common/api.service\';'),
    (L, 'Define and export the store. The first argument is a unique id; it is '
        'what the Vue DevTools label the store with.'),
    (LC, 'export const useHomeStore = defineStore(\'home\', {'),
    (LC, '});'),
    (L, 'Add the state. As in a component, state is a function that returns a '
        'fresh object.'),
    (LC, '  state: () => ({'),
    (LC, '    tags: [],'),
    (LC, '    articles: [],'),
    (LC, '    isLoading: true,'),
    (LC, '    articlesCount: 0,'),
    (LC, '  }),'),
    (LS, 'The Vuex version of this store also declared getters called articles, '
         'isLoading, articlesCount and tags that just returned the matching piece '
         'of state. In Pinia, state is exposed on the store directly, so those '
         'pass-through getters are unnecessary. Keep getters for values you '
         'actually derive.'),
    (L, 'Add the actions. An action can be async, and assigns to state through '
        'this — there is no commit and no mutation to write.'),
    (LC, '  actions: {'),
    (LC, '    async fetchArticles(params = {}) {'),
    (LC, '      this.isLoading = true;'),
    (LC, ''),
    (LC, '      try {'),
    (LC, '        const { data } = await ArticlesService.query('),
    (LC, '          params.type,'),
    (LC, '          params.filters,'),
    (LC, '        );'),
    (LC, ''),
    (LC, '        this.articles = data.articles;'),
    (LC, '        this.articlesCount = data.articlesCount;'),
    (LC, '      } finally {'),
    (LC, '        this.isLoading = false;'),
    (LC, '      }'),
    (LC, '    },'),
    (LC, '  },'),
    (LS, 'The finally block guarantees the loading flag is cleared even if the '
         'request fails, which the Vuex version did not do.'),
    (L, 'Add two more actions, setTags and updateArticleInList, replacing the '
        'mutations of the same names.'),
    (LC, '    setTags(tags) {'),
    (LC, '      this.tags = tags;'),
    (LC, '    },'),
    (LC, ''),
    (LC, '    updateArticleInList(data) {'),
    (LC, '      this.articles = this.articles.map((article) =>'),
    (LC, '        article.slug === data.slug'),
    (LC, '          ? {'),
    (LC, '              ...article,'),
    (LC, '              favorited: data.favorited,'),
    (LC, '              favoritesCount: data.favoritesCount,'),
    (LC, '            }'),
    (LC, '          : article,'),
    (LC, '      );'),
    (LC, '    },'),
    (L, 'Import the store and storeToRefs into ArticleList.vue'),
    (LC, 'import { storeToRefs } from \'pinia\';'),
    (LC, ''),
    (LC, 'import { useHomeStore } from \'../stores/home\';'),
    (L, 'Call the store’s composable and pull out the pieces you need.'),
    (LC, 'const homeStore = useHomeStore();'),
    (LC, 'const { articles, isLoading } = storeToRefs(homeStore);'),
    (NOTE, 'Note: a Pinia store is a reactive object, so destructuring it directly '
           'would break reactivity — you would copy the values out and never see '
           'an update. storeToRefs converts state and getters into refs that keep '
           'tracking. Actions are plain functions and can be destructured '
           'normally, or called on the store as we do below.'),
    (L, 'Remove the local articles ref from ArticleList.vue — the store owns that '
        'state now.'),
    (L, 'Change the onMounted hook to call the store action.'),
    (LC, 'onMounted(() => {'),
    (LC, '  homeStore.fetchArticles({ type: \'all\' });'),
    (LC, '});'),
    (LS, 'Compare that with the Vuex version, which read '
         'this.$store.dispatch(FETCH_ARTICLES, this.listConfig) and needed a '
         'string constant and a computed property to build the payload.'),
    (L, 'Add a v-if directive to the ArticleList template to hide the list until '
        'the request has finished.'),
    (LC, '<template>'),
    (LC, '  <div>'),
    (LC, '    <div v-if="isLoading" class="article-preview">Loading articles...</div>'),
    (LC, '    <div v-else>'),
    (LC, '      <input'),
    (LC, '        v-model="searchDetails"'),
    (LC, '        class="form-control"'),
    (LC, '        placeholder="filter articles"'),
    (LC, '      />'),
    (LC, '      <div v-if="articles.length === 0" class="article-preview">'),
    (LC, '        No articles are here... yet.'),
    (LC, '      </div>'),
    (LC, '      <ArticlePreview'),
    (LC, '        v-for="(article, index) in filterIt"'),
    (LC, '        :key="article.title + index"'),
    (LC, '        :style="{ fontSize: articleFontSize + \'em\' }"'),
    (LC, '        :article="article"'),
    (LC, '        @enlarge-text="articleFontSize += 0.1"'),
    (LC, '      />'),
    (LC, '    </div>'),
    (LC, '  </div>'),
    (LC, '</template>'),
    (L, 'Start the development server and view the app in a browser.'),
    (L, 'Open the Vue DevTools and find the Pinia tab. Watch isLoading flip as the '
        'request completes, and try editing articles directly from the '
        'inspector.'),
    (L, 'Challenge: display tags along with each article preview.'),
    (L, 'Challenge: populate the Popular Tags box with a list of tags from the '
        'currently displayed article previews.'),
    (L, 'Challenge: clicking on a tag in the list of popular tags should filter '
        'the display of articles.'),
    (N, ''),
]

# ------------------------------------------------------ Lab 21 (1110-1220)
LAB21 = [
    (H1, 'Lab 21: Routing'),
    (N, 'So far, our application only has one screen. In this lab, you’ll start to '
        'implement additional routes. Routing in modern JavaScript frameworks '
        'works by reacting to changes in the browser address to load or show '
        'different views. In reality everything is happening in the same HTML '
        'page, but the data and view change. This is what we mean by a Single '
        'Page Application (or SPA).'),
    (N, ''),
    (N, 'In this lab, you’ll install and configure Vue Router, and then create the '
        'first two additional routes for this application: Sign In and Sign Up.'),
    (N, ''),
    (L, 'Install vue-router.'),
    (LC, 'npm install vue-router'),
    (L, 'Make a new directory in src named router.'),
    (L, 'Create a file named index.js inside src/router'),
    (L, 'Import the router factory functions. Vue Router 4 and later are created '
        'with a function rather than a constructor, and are not installed with '
        'Vue.use.'),
    (LC, 'import { createRouter, createWebHistory } from \'vue-router\';'),
    (NOTE, 'Note: this is the biggest API change from Vue Router 3. new Router() '
           'becomes createRouter(); the mode: \'history\' option becomes '
           'createWebHistory(); mode: \'hash\' becomes createWebHashHistory(); '
           'and the catch-all path \'*\' becomes \'/:pathMatch(.*)*\'.'),
    (L, 'Create and export the router, passing it a history implementation and a '
        'routes array.'),
    (LC, 'export default createRouter({'),
    (LC, '  history: createWebHistory(import.meta.env.BASE_URL),'),
    (LC, '  routes: [],'),
    (LC, '});'),
    (LS, 'createWebHistory uses the HTML5 History API, so URLs have no #. That is '
         'why the "/#/" you may have seen in older versions of this app is gone.'),
    (L, 'Make the first (default) route. Remember the .vue extension in the '
        'dynamic import.'),
    (LC, '  routes: ['),
    (LC, '    {'),
    (LC, '      name: \'home\','),
    (LC, '      path: \'/\','),
    (LC, '      component: () => import(\'@/components/Home.vue\'),'),
    (LC, '    },'),
    (LC, '  ],'),
    (LS, 'Writing the component as an arrow function that returns an import() '
         'makes it a lazily-loaded route: Vite gives that route its own JavaScript '
         'chunk, which is not downloaded until the route is visited.'),
    (L, 'Import the router module into main.js and install it on the app.'),
    (LC, 'import router from \'./router\';'),
    (LC, ''),
    (LC, 'app.use(createPinia());'),
    (LC, 'app.use(router);'),
    (LC, 'app.mount(\'#app\');'),
    (LS, 'Install Pinia before the router, so that navigation guards and route '
         'components can reach the stores.'),
    (L, 'Open App.vue and replace the <Home /> component with <RouterView />.'),
    (LC, '<script setup>'),
    (LC, 'import { RouterView } from \'vue-router\';'),
    (LC, ''),
    (LC, 'import Header from \'./components/Header.vue\';'),
    (LC, 'import Footer from \'./components/Footer.vue\';'),
    (LC, '</script>'),
    (LC, ''),
    (LC, '<template>'),
    (LC, '  <div id="app">'),
    (LC, '    <Header />'),
    (LC, '    <RouterView />'),
    (LC, '    <Footer />'),
    (LC, '  </div>'),
    (LC, '</template>'),
    (LS, 'app.use(router) does register <RouterView> and <RouterLink> globally, so '
         'the import is optional. Importing them explicitly is worth the one line: '
         'the editor can then resolve them, and the component says what it '
         'depends on.'),
    (L, 'Remove the import for Home from App.vue.'),
    (L, 'Run the development server and open the application in your browser. It '
        'should work the same as before.'),
    (L, 'Open the Header component for editing.'),
    (L, 'Find the Sign In link, and replace it with a RouterLink component:'),
    (LC, '<RouterLink'),
    (LC, '  class="nav-link"'),
    (LC, '  active-class="active"'),
    (LC, '  :to="{ name: \'login\' }"'),
    (LC, '>'),
    (LC, '  Sign in'),
    (LC, '</RouterLink>'),
    (NOTE, 'Note: the exact prop that Vue Router 3 needed here is gone. In Vue '
           'Router 4 and later, active-class is applied on partial matches and '
           'exact-active-class on exact ones, so use exact-active-class if you '
           'need the old behaviour.'),
    (L, 'View the application in your browser and click on the Sign In link. It '
        'won’t work yet, because the login route doesn’t exist.'),
    (L, 'Create a new route, in router/index.js, with the name login and the path '
        '/login.'),
    (LC, '    {'),
    (LC, '      name: \'login\','),
    (LC, '      path: \'/login\','),
    (LC, '      component: () => import(\'@/components/Login.vue\'),'),
    (LC, '    },'),
    (L, 'Make a new component named Login and put a login form in the '
        '<template>:'),
    (LC, '<script setup>'),
    (LC, '// The form is wired up to the auth store in the next lab.'),
    (LC, 'function onSubmit() {}'),
    (LC, '</script>'),
    (LC, ''),
    (LC, '<template>'),
    (LC, '  <div>'),
    (LC, '    <h1>Log In Here</h1>'),
    (LC, '    <form @submit.prevent="onSubmit">'),
    (LC, '      <fieldset class="form-group">'),
    (LC, '        <input'),
    (LC, '          class="form-control form-control-lg"'),
    (LC, '          type="text"'),
    (LC, '          placeholder="Email"'),
    (LC, '        />'),
    (LC, '      </fieldset>'),
    (LC, '      <fieldset class="form-group">'),
    (LC, '        <input'),
    (LC, '          class="form-control form-control-lg"'),
    (LC, '          type="password"'),
    (LC, '          placeholder="Password"'),
    (LC, '        />'),
    (LC, '      </fieldset>'),
    (LC, '      <button class="btn btn-lg btn-primary pull-xs-right">Sign in</button>'),
    (LC, '    </form>'),
    (LC, '  </div>'),
    (LC, '</template>'),
    (L, 'Use <RouterLink> to link the logo to the home page.'),
    (LC, '<RouterLink class="navbar-brand" :to="{ name: \'home\' }">'),
    (LC, '  Logo'),
    (LC, '</RouterLink>'),
    (L, 'Link the Home navigation link to the home page the same way.'),
    (L, 'Challenge: make the Sign Up page and route.'),
    (L, 'Challenge: use a <RouterView> inside Home.vue to render a different list '
        '(or differently-styled list) of articles when the user clicks a link. '
        'HINT: add a children property to the home route and make it an array of '
        'route objects.'),
    (N, ''),
]

# ------------------------------------------------------ Lab 22 (1221-1259)
LAB22 = [
    (H1, 'Lab 22: AJAX'),
    (N, 'In this lab, you’ll implement sign up functionality along with login and '
        'checking of authorization.'),
    (N, ''),
    (L, 'Copy jwt.service.js and api.service.js from labs/lab22/common into '
        'src/common, overwriting your existing api.service.js.'),
    (LS, 'The new api.service.js adds the get, post, put and delete helpers the '
         'auth store needs, plus a setHeader() method that attaches the stored '
         'token to every subsequent request.'),
    (L, 'Copy stores/auth.js from labs/lab22/stores into src/stores.'),
    (L, 'Open src/stores/auth.js and read through it. Note the shape:'),
    (LS, 'state holds errors, user, and isAuthenticated, which is seeded from '
         'whatever token is already in localStorage.'),
    (LS, 'setAuth and purgeAuth are ordinary actions. In the Vuex version these '
         'were the SET_AUTH and PURGE_AUTH mutations, referred to through string '
         'constants in mutations.type.js. Pinia needs neither the constants nor '
         'the file.'),
    (LS, 'login, register, checkAuth and updateUser are async actions that call '
         'the API and then call setAuth. They store the server’s validation errors '
         'on state.errors and re-throw, so the component can decide what to do.'),
    (L, 'Delete src/store, along with actions.type.js and mutations.type.js. '
        'Nothing imports them any more.'),
    (L, 'Copy Login.vue and Register.vue from labs/lab22/components, overwriting '
        'your existing Login component.'),
    (L, 'Open Login.vue and note how the component talks to the store.'),
    (LC, 'const router = useRouter();'),
    (LC, 'const authStore = useAuthStore();'),
    (LC, 'const { errors } = storeToRefs(authStore);'),
    (LC, ''),
    (LC, 'async function onSubmit() {'),
    (LC, '  try {'),
    (LC, '    await authStore.login({ email: email.value, password: password.value });'),
    (LC, '    router.push({ name: \'home\' });'),
    (LC, '  } catch {'),
    (LC, '    // Errors are surfaced through the store\'s `errors` state.'),
    (LC, '  }'),
    (LC, '}'),
    (NOTE, 'Note: inside <script setup> there is no this, so this.$router and '
           'this.$store are not available. useRouter() and the store’s own '
           'use-function are the Composition API equivalents. useRoute() gives you '
           'the current route object.'),
    (L, 'Add the register route to router/index.js, pointing at Register.vue.'),
    (L, 'Test it out by registering and then by logging in.'),
    (L, 'Import the auth store and storeToRefs into Home.vue'),
    (LC, 'import { storeToRefs } from \'pinia\';'),
    (LC, ''),
    (LC, 'import { useAuthStore } from \'@/stores/auth\';'),
    (LC, ''),
    (LC, 'const { isAuthenticated } = storeToRefs(useAuthStore());'),
    (LS, 'The Vuex version used ...mapGetters([\'isAuthenticated\']) inside a '
         'computed option. storeToRefs is the direct replacement, and it works on '
         'state as well as getters.'),
    (L, 'Use isAuthenticated in Home.vue to conditionally show a logged-in user '
        'message in the sidebar.'),
    (LC, '<p v-if="isAuthenticated">Welcome, authenticated user</p>'),
    (NOTE, 'Note: the Vue 2 version of these components displayed errors with a '
           'filter — {{ v | error }}. Filters were removed in Vue 3. Use a method, '
           'a computed property, or an inline expression instead; Login.vue joins '
           'the array of messages inline.'),
    (L, 'Challenge: display a logout button instead of the Login and Sign Up '
        'buttons when a user is logged in.'),
    (L, 'Challenge: call the auth store’s checkAuth() action when the app starts, '
        'so a returning user with a valid token is logged straight back in.'),
    (N, ''),
]

# ------------------------------------------------------ Lab 23 (1260-1265)
LAB23 = [
    (H1, 'Lab 23: Testing with Vitest'),
    (N, 'If you run the unit tests in your project now, you’ll see that the test '
        'on Home.vue fails. Home.vue now depends on the router and on a Pinia '
        'store, and neither exists inside a bare mount(). In this lab, you’ll '
        'learn how to provide them.'),
    (N, ''),
    (L, 'Run npm run test and read the failure carefully. The message names the '
        'injection that could not be resolved.'),
    (L, 'Visit https://test-utils.vuejs.org/guide/ and read about the '
        'global.plugins mounting option.'),
    (NOTE, 'Note: Vue Test Utils 1 used createLocalVue() to install plugins '
           'without polluting the global Vue. Vue 3 apps are already isolated, so '
           'createLocalVue is gone — plugins are passed per-mount through '
           'global.plugins.'),
    (L, 'Open tests/components/Home.spec.js and create a router for the test.'),
    (LC, 'import { createRouter, createWebHistory } from \'vue-router\';'),
    (LC, ''),
    (LC, 'const router = createRouter({'),
    (LC, '  history: createWebHistory(),'),
    (LC, '  routes: ['),
    (LC, '    { name: \'home\', path: \'/\', component: { template: \'<div />\' } },'),
    (LC, '  ],'),
    (LC, '});'),
    (L, 'Create a fresh Pinia instance before each test.'),
    (LC, 'import { createPinia, setActivePinia } from \'pinia\';'),
    (LC, ''),
    (LC, 'let pinia;'),
    (LC, ''),
    (LC, 'beforeEach(() => {'),
    (LC, '  pinia = createPinia();'),
    (LC, '  setActivePinia(pinia);'),
    (LC, '});'),
    (LS, 'Creating the Pinia instance per test keeps store state from leaking from '
         'one test into the next.'),
    (L, 'Pass both plugins when you mount the component.'),
    (LC, 'const createWrapper = () ='),
    (LC, '  shallowMount(Home, { global: { plugins: [pinia, router] } });'),
    (LS, 'shallowMount stubs out child components, so GlobalFeed never mounts and '
         'no HTTP request is made from the test.'),
    (L, 'Run npm run test again and confirm every test passes.'),
    (L, 'Challenge: write a test for the auth store itself. A Pinia store can be '
        'tested without mounting any component — call useAuthStore() after '
        'setActivePinia() and assert on its state.'),
    (L, 'Challenge: use vi.mock() to fake the api.service module so the store test '
        'never touches the network.'),
    (N, ''),
]

# ---------------------------------------------------------- Lab 24 (1266-)
LAB24 = [
    (H1, 'Lab 24: Transitions and Animations'),
    (N, 'Vue’s built-in <Transition> component applies CSS classes at each stage '
        'of an element entering or leaving the DOM, so you can animate it with '
        'plain CSS.'),
    (NOTE, 'Note: the class names changed in Vue 3. What Vue 2 called v-enter and '
           'v-leave-to are now v-enter-from and v-leave-to, and the starting class '
           'for a leave transition is v-leave-from. If you copy an example from an '
           'old blog post and nothing animates, this is usually why.'),
    (L, 'Add a Remove From Feed icon (maybe a trash can) to each article.'),
    (L, 'When clicked, it should remove the article from the feed.'),
    (L, 'Wrap the list in a <TransitionGroup> and animate articles as they leave.'),
    (LC, '<TransitionGroup name="article" tag="div">'),
    (LC, '  <ArticlePreview'),
    (LC, '    v-for="(article, index) in filterIt"'),
    (LC, '    :key="article.slug"'),
    (LC, '    :article="article"'),
    (LC, '  />'),
    (LC, '</TransitionGroup>'),
    (LS, 'Every child of a <TransitionGroup> needs a stable, unique key. Using the '
         'array index will make the animation attach to the wrong element.'),
    (L, 'Write the transition classes.'),
    (LC, '.article-enter-from,'),
    (LC, '.article-leave-to {'),
    (LC, '  opacity: 0;'),
    (LC, '  transform: translateX(30px);'),
    (LC, '}'),
    (LC, ''),
    (LC, '.article-enter-active,'),
    (LC, '.article-leave-active {'),
    (LC, '  transition: all 0.3s ease;'),
    (LC, '}'),
    (L, 'Challenge: add .article-move so the remaining articles slide up smoothly '
        'to fill the gap.'),
    (N, ''),
]

# TOC entries whose titles changed.
TOC_RENAMES = {
    'Lab 02: Get Started with vue-cli': 'Lab 02: Get Started with Vite',
    'Lab 19: Mixins': 'Lab 19: Composables',
    'Lab 20: Implementing Vuex': 'Lab 20: Implementing Pinia',
    'Lab 23: Testing with Jest': 'Lab 23: Testing with Vitest',
}

# Targeted single-paragraph rewrites in sections that are otherwise unchanged.
# Keyed by an exact-prefix match on the v1.5 paragraph text.
TWEAKS = [
    # Lab 04
    ('Make the new .vue files for the Home and Footer components',
     'Make the new .vue files for the Home and Footer components (inside '
     'src/components) and create <script setup> and <template> sections for '
     'each.'),
    ('Import Footer and Home into App.vue and add them to the components',
     'Import Footer and Home into App.vue. With <script setup> the import is '
     'the registration — there is no components property to add them to.'),
    ('Run npm run serve and preview your app so far in a browser.',
     'Run npm run dev and preview your app so far in a browser.'),
    # Lab 06
    ('Enter npm install npm -g',
     'Enter npm ls -g --depth=0'),
    ('This command will install the latest version of npm.',
     'This command lists the packages that are installed globally on your '
     'computer. npm ships with Node.js, so the way to update it is normally to '
     'install a newer Node.js release rather than to update npm on its own.'),
    ('Note: If the installation of npm fails on MacOSX, you may need to preface it',
     'Note: a global npm install writes outside your home directory. If one '
     'fails with a permissions error on macOS or Linux, prefer a Node version '
     'manager such as nvm or fnm over running npm with sudo.'),
    ('Enter npm -v to see what version of npm is now installed.',
     'Enter npm ls to see the packages installed in the current project only.'),
    ('Enter npm ls -g',
     'Enter npm outdated'),
    ('This command will list all the packages that are installed on your computer currently.',
     'This command compares the versions in your project against the registry '
     'and lists anything with a newer release available.'),
    # Lab 12
    ('If it\'s not already running, start up your development server by running npm run serve.',
     'If it’s not already running, start up your development server by running '
     'npm run dev. Open your browser and go to http://localhost:5173.'),
    # Lab 18
    ('Populate the list of tags in the 2nd column dynamically from the feed at /tags',
     'Populate the list of tags in the 2nd column dynamically from the feed at '
     '/tags (using the same base URL as the articles feed). Use slots so that '
     'the TagList component decides the layout and its parent supplies the '
     'content.'),
    ('Make clicking on the tags in the tag box filter the list of articles.',
     'Make clicking on the tags in the tag box filter the list of articles. '
     'Emit an event from Tag.vue with defineEmits and handle it in Home.vue.'),
    # Lab 10 / general
    ('Enter npm run serve to start the vue-cli development web server.',
     'Enter npm run dev to start the Vite development server.'),
]
